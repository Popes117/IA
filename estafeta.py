class Estafeta:
    
    #acho que nao precisa ter aqui localização
    def __init__(self, id, nome, avaliacao, localizacao):
        self.id = id
        self.nome = nome
        self.avaliacao = avaliacao
        self.localizacao = localizacao

    def changeLocal(self, newLocal: str):
        self.localizacao = newLocal


    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getAvaliacao(self):
        return self.avaliacao