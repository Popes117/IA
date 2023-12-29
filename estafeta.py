class Estafeta:
    
    #acho que nao precisa ter aqui localização
    def __init__(self, id, nome, somaAvaliacao, nrEncomendas):
        self.id = id
        self.nome = nome
        self.somaAvaliacao = somaAvaliacao
        #self.localizacao = localizacao
        self.nrEncomendas = nrEncomendas

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
        return self.somaAvaliacao / self.nrEncomendas

    #def move(self, newLocal: str):
    #    self.localizacao = newLocal
