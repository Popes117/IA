#Inteligência Artificial
#2022/23


#NegaWatt
class Estafeta:
    
    def __init__(self,nome: str, aval: int, localizacao: str):
        self.nome = nome
        self.aval = aval
        self.localizacao = localizacao

    def changeLocal(self, newLocal: str):
        self.localizacao = newLocal
