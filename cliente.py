class Cliente:
    
    def __init__(self, id, nome, morada):
        self.id = id
        self.nome = nome
        self.morada = morada
    
    def getId(self):
        return self.id
    
    def getRua(self):
        return self.morada
