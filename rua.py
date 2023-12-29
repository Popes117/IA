#Ruas vão ser os nodos para os grafos
class Rua:
    def __init__(self, nome, freguesia):
        self.nome = nome
        self.freguesia = freguesia

    def __str__(self):
        return self.nome + "," + self.freguesia

    def __repr__(self) -> str:
        return str(self)

    def getNome(self):
        return self.nome

    def getFreguesia(self):
        return self.freguesia
    
    def getRua(self):
        return (", ".join([self.nome,self.freguesia]))

    def __hash__(self):
        # Combine os hashes dos atributos que compõem a identidade do objeto
        return hash((self.nome, self.freguesia))

    def __eq__(self, other):
        # Verifique se os atributos que compõem a identidade são iguais
        return (isinstance(other, Rua) and
                self.nome == other.nome and
                self.freguesia == other.freguesia)