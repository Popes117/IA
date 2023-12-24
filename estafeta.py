class Estafeta:
    
    #acho que nao precisa ter aqui localização
    def __init__(self, id, nome, avaliacao, transport):
        self.id = id
        self.nome = nome
        self.avaliacao = avaliacao
        #self.localizacao = localizacao
        self.transport = transport

    #def changeLocal(self, newLocal: str):
    #    self.localizacao = newLocal


    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getAvaliacao(self):
        return self.avaliacao

    #def move(self, newLocal: str):
    #    self.localizacao = newLocal
