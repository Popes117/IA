from transporte import *

class Estafeta:
    listaEstafeta = [] #mudar para dicionario talvez seja melhor
    ultimo_id = 0
    
    #acho que nao precisa ter aqui localização
    def __init__(self, id, nome, somaAvaliacao, nrEncomendas):
        self.id = id
        self.nome = nome
        self.somaAvaliacao = somaAvaliacao
        self.nrEncomendas = nrEncomendas
        Estafeta.listaEstafeta.append(self)
        Estafeta.ultimo_id = id
        

    #def changeLocal(self, newLocal: str):
    #    self.localizacao = newLocal


    def getId(self):
        return self.id

    def getNome(self):
        return self.nome
    
    def getSomaAval(self):
        return self.somaAvaliacao
    
    def getNrEnc(self):
        return self.nrEncomendas

    def getAvaliacao(self):
        if self.nrEncomendas == 0:
            return 0
        return round((self.somaAvaliacao / self.nrEncomendas),2)
    

    #provavelmente será necessario acrescentar a mudança na lista!!!
    def updateSomaAval(self, aval):
        self.somaAvaliacao += aval

    def updateNrEnc(self):
        self.nrEncomendas += 1
        

    #def move(self, newLocal: str):
    #    self.localizacao = newLocal

    def __str__(self):
        return "("+ str(self.id) + ", " + self.nome + ", " + str(self.getAvaliacao()) + ")"

    def __repr__(self) -> str:
        return str(self)


    def adicionarEstafeta(nome, soma, nr):
        id = Estafeta.ultimo_id + 1
        Estafeta(id, nome, soma, nr)

    def updateAvaliacao(self,aval):
        self.somaAvaliacao += aval
        self.nrEncomendas += 1

    def chooseTransport(self,peso,custo,tempoLimite):
        mota = True
        bicla = True

        if peso > 5:
            bicla = False
        if peso > 20:
            mota = False
        tempoBicla = (custo/(10-(peso*0.6))) * 60
        tempoMota = (custo/(35-(peso*0.5))) * 60
        tempoCarro =(custo/(50-(peso*0.1))) * 60

        atrasoDesejado = tempoLimite + tempoLimite*(self.somaAvaliacao/self.nrEncomendas)/5
        print(f"Tempo Bicla: {tempoBicla}")
        print(f"Tempo Mota: {tempoMota}")
        print(f"Tempo Max: {atrasoDesejado}")
        if tempoBicla <= atrasoDesejado and bicla:
            return "Bicicleta",tempoBicla
        if tempoMota <= atrasoDesejado and mota:
            return "Mota",tempoMota
        else:
            return "Carro",tempoCarro


    
def carregarEstafetas(nome_ficheiro):
    with open(nome_ficheiro, 'r') as ficheiro:
        for linha in ficheiro:
            campo = linha.strip().split(',')
            id_estafeta = int(campo[0])
            nome_estafeta = campo[1]
            soma_avaliacao = int(campo[2])
            nr_encomendas = int(campo[3])
            Estafeta(id_estafeta, nome_estafeta,soma_avaliacao,nr_encomendas)
            #print(Estafeta.listaEstafeta)

def guardarEstafetas(nome_ficheiro):
    with open(nome_ficheiro, 'w') as ficheiro:
        for estafeta in Estafeta.listaEstafeta:
            linha = f"{estafeta.getId()},{estafeta.getNome()},{estafeta.getSomaAval()},{estafeta.getNrEnc()}\n"
            ficheiro.write(linha)



    
