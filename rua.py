#Ruas vão ser os nodos para os grafos
class Rua:
    def __init__(self, nome, freguesia):
        self.nome = nome
        self.freguesia = freguesia

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

    def getNome(self):
        return self.nome

    def getFreguesia(self):
        return self.freguesia

    def __eq__(self,other): 
        return self.nome == other.nome # são iguais se nome igual