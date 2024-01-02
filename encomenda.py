import datetime
from rua import *

class Encomenda:
    listaEncomendas = {}
    ultimo_id = 0


    def __init__(self, id, id_cliente, peso, volume, prazo_limite, morada_entrega, data):
        self.id = id
        self.id_cliente = id_cliente
        #self.id_estafeta = id_estafeta
        self.peso = peso
        self.volume = volume
        self.prazo_limite = prazo_limite
        self.morada_entrega = morada_entrega
        self.data = datetime.datetime.strptime(data, '%d/%m/%Y').strftime('%d/%m/%Y') #formato das datas seria passado com dia/mes/ano
        Encomenda.listaEncomendas[self.id] = self
        Encomenda.ultimo_id = id

    def __str__(self):
        return "("+str(self.id)+", "+str(self.id_cliente)+", "+str(self.peso)+", "+str(self.volume)+", "+str(self.prazo_limite) + ", " +self.morada_entrega.getRua() + ", " +str(self.data) +")"
    
    def __repr__(self) -> str:
        return str(self)
    
    
    def getId(self):
        return self.id
    
    def getIDCliente(self):
        return self.id_cliente

    def getPeso(self):
        return self.peso
    
    def getVolume(self):
        return self.volume
    
    def getPrazo(self):
        return self.prazo_limite
    
    def getMorada(self):
        return self.morada_entrega

    def getData(self): #passei para isto para facilitar no registo dos clientes
        return self.data
    

    def adicionarEncomenda(id_cliente, peso, volume, prazo, morada, data):
        id = Encomenda.ultimo_id + 1
        Encomenda(id, id_cliente, peso, volume, prazo, morada, data)
        return id
    

#!erros são para tirar!
def carregarEncomendas(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            for linha in ficheiro:

                campo = linha.strip().split(',')
                id = int(campo[0])
                id_cliente = int(campo[1])
                peso = float(campo[2])
                volume = float(campo[3])
                tempoMaximo = int(campo[4])
                morada = Rua(campo[5],campo[6].strip())
                data = campo[7]
                Encomenda(id, id_cliente,peso,volume,tempoMaximo,morada,data)
    except FileNotFoundError:
        print(f"O arquivo {nome_ficheiro} não foi encontrado.")
    except PermissionError:
        print(f"Sem permissão para ler o arquivo {nome_ficheiro}.")
    except Exception as e:
        print(f"Erro ao ler o arquivo {nome_ficheiro}: {e}")


def guardarEncomendas(nome_ficheiro):
    with open(nome_ficheiro, 'w') as ficheiro:
        for encomenda in Encomenda.listaEncomendas.values():
            linha = f"{encomenda.getId()},{encomenda.getIDCliente()},{encomenda.getPeso()},{encomenda.getVolume()},{encomenda.getPrazo()},{encomenda.getMorada().getRua()},{encomenda.getData()}\n"
            ficheiro.write(linha)



#as encomendas vão ser agrupadas por datas, se tiveram a mesma data são colocadas na mesma lista.
#caso não encontre, adicionalmente caso a soma do peso delas passe dos 50kg a mais recente é inserida numa nova lista
def agruparEncomendas():
    encomendas_agrupadas = {}
    pesoMaximo = 50.0

    for encomenda_id, encomenda in Encomenda.listaEncomendas.items():
        # Verifica se a data já está presente no dicionário
        if encomenda.data in encomendas_agrupadas:
            grupos_data = encomendas_agrupadas[encomenda.data]
        else:
            grupos_data = []
            encomendas_agrupadas[encomenda.data] =  grupos_data

        adicionada = False
        for grupo_atual in grupos_data:
            #Verifica se nova encomenda cabe dentro dos limites de peso
            if grupo_atual['peso'] + encomenda.peso <= pesoMaximo: 
                grupo_atual['encomendas'].append(encomenda_id)
                grupo_atual['peso'] += encomenda.peso
                adicionada = True
                break

        #Caso não seja possível colocar numa lista já existente, cria um novo grupo
        if not adicionada:
            novo_grupo = {'encomendas': [encomenda_id], 'peso': encomenda.peso}
            grupos_data.append(novo_grupo)
            
    return encomendas_agrupadas