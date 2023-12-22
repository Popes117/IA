class Transporte:

    def __init__(self, tipo, capacidade_max, velocidade_max):
        self.tipo = tipo                      #bicicleta, moto ou carro
        self.capacidade_max = capacidade_max  #5, 20 ou 100
        self.velocidade_max = velocidade_max  #10, 35 ou 50


    def getTipo(self):
        return self.tipo

    def getCapacidade(self):
        return self.capacidade_max
    
    def getVelocidade(self):
        return self.velocidade_max