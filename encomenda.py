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
        self.data = datetime.strptime(data, '%d/%m/%Y') #formato das datas seria passado com dia/mes/ano
        Encomenda.listaEncomendas[self.id] = self
        Encomenda.ultimo_id = id

    def __str__(self):
        return "("+str(self.id)+", "+str(self.id_cliente)+", "+str(self.peso)+", "+str(self.volume)+", "+str(self.prazo_limite) + ", " +self.morada_entrega.getRua() + str(self.data) +")"
    
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



def carregarEncomendas(nome_ficheiro):
    with open(nome_ficheiro, 'r') as ficheiro:
        for linha in ficheiro:
            campo = linha.strip().split(',')
            id = int(campo[0])
            id_cliente = int(campo[1])
            peso = int(campo[2])
            volume = int(campo[3])
            tempoMaximo = int(campo[4])
            morada = Rua(campo[5], campo[6])
            data = campo[7]
            Encomenda(id, id_cliente,peso,volume,tempoMaximo,morada,data)


def guardarEncomendas(nome_ficheiro):
    with open(nome_ficheiro, 'w') as ficheiro:
        for encomenda in Encomenda.listaEncomendas:
            linha = f"{encomenda.getId()},{encomenda.getIDCliente()},{encomenda.getPeso()},{encomenda.getVolume()},{encomenda.getPrazo()},{encomenda.getMorada()},{encomenda.getData()}\n"
            ficheiro.write(linha)

def preco(peso, volume, transporte):
    if transporte == "Bicicleta":
        return 1 + peso*volume/100
    elif transporte == "Bicicleta":
        return 3 + 2*peso*volume/100
    else:
        return 5 + 4*peso*volume/100

"""
#as encomendas vão ser agrupadas por datas, se tiveram a mesma data são colocadas na mesma lista. caso não encontre
def agrupar_encomendas_por_data():
    encomendas_agrupadas = {}
    
    for encomenda_id, encomenda in Encomenda.listaEncomendas.items():
        # Verifica se a data já está presente no dicionário
        if encomenda.data in encomendas_agrupadas:
            encomendas_agrupadas[encomenda.data].append(encomenda)
        else:
            encomendas_agrupadas[encomenda.data] = [encomenda]

    return encomendas_agrupadas

def atualizar_encomendas_agrupadas(self):
        # Atualiza apenas o grupo relevante para esta encomenda
        if self.data in Encomenda.encomendasAgrupadas:
            Encomenda.encomendasAgrupadas[self.data].append(self)
        else:
            Encomenda.encomendasAgrupadas[self.data] = [self]
"""
