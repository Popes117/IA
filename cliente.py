class Cliente:
    clientes = {}
    ultimoId = 0 #incrementa sempre que fizer o registo de um novo

    def __init__(self, id, nome, morada):
        self.id = id
        self.nome = nome
        self.morada = morada
    
    def getId(self):
        return self.id
    
    def getRua(self):
        return self.morada
    
    def __str__(self):
        return "("+ str(self.id) + ", " + self.nome + ", " + self.morada.getRua() + ")"

    def __repr__(self) -> str:
        return str(self)
    