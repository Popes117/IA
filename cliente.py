class Cliente:
    
    def __init__(self, nome, morada, id):
        self.id = id
        self.nome = nome
        self.morada = morada
    
    def getId(self):
        return self.id
    
    def getRua(self):
        return self.morada
