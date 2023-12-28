class Heu:

    def __init__(self):
        self.heuristicas = list()

    def fillHeuristicas(self):
        heuristicasRuadaConfeiteira= {
            "Rua da Confeiteira":0,
            "Rua de Redondo":2.4,
            "Rua de São Martinho":1.9,
            "Rua 5 de Outubro":1.2,
            "Rua da Universidade":3.3,
            "Rua Santa Margarida":2.3,
            "Rua de São José":2.7,
            "Rua do Raio":2.9,
            "Avenida Dom Joao II":3.6, 
            "Rua do Fujacal":2.7,
            "Rua Joãozinho Azeredo":2.6, 
            "Rua da Igreja":4.5, 
            "Rua da Senra":4.1
        }
        heuristicasRuadeRedondo= {
            "Rua de Redondo":0,
            "Rua de São Martinho":3.0,
            "Rua 5 de Outubro":2.1,
            "Rua da Universidade":1.4,
            "Rua Santa Margarida":2.0,
            "Rua de São José":1.7,
            "Rua do Raio":2.0,
            "Avenida Dom Joao II":2.0, 
            "Rua do Fujacal":2.6,
            "Rua Joãozinho Azeredo":3.2, 
            "Rua da Igreja":4.0,
            "Rua da Senra":4.2
        }
        heuristicasRuadeSãoMartinho= {
            "Rua de São Martinho":0,
            "Rua 5 de Outubro":1.1,
            "Rua da Universidade":3.5,
            "Rua Santa Margarida":1.2,
            "Rua de São José":2.0,
            "Rua do Raio":1.9,
            "Avenida Dom Joao II":2.8, 
            "Rua do Fujacal":1.4,
            "Rua Joãozinho Azeredo":0.8, 
            "Rua da Igreja":2.5, 
            "Rua da Senra":1.8
        }
        heuristicasCabeceiras= {
            "Rua 5 de Outubro":0,
            "Rua da Universidade":2.9,
            "Rua Santa Margarida":1.0,
            "Rua de São José":1.5,
            "Rua do Raio":1.6,
            "Avenida Dom Joao II":2.7, 
            "Rua do Fujacal":1.9,
            "Rua Joãozinho Azeredo":1.8, 
            "Rua da Igreja":3.0, 
            "Rua da Senra":2.8
        }
        heuristicasCelorico= {
            "Rua da Universidade":0,
            "Rua Santa Margarida":1.9,
            "Rua de São José":1.4,
            "Rua do Raio":1.6,
            "Avenida Dom Joao II":1.3, 
            "Rua do Fujacal":2.6,
            "Rua Joãozinho Azeredo":3.1, 
            "Rua da Igreja":2.9, 
            "Rua da Senra":3.3
        }
        heuristicaRuaSantaMargarida= {
            "Rua Santa Margarida":0,
            "Rua de São José":0.8,
            "Rua do Raio":0.7,
            "Avenida Dom Joao II":1.6, 
            "Rua do Fujacal":1.0,
            "Rua Joãozinho Azeredo":1.2, 
            "Rua da Igreja":2.4, 
            "Rua da Senra":2.7
        }
        heuristicasRuadeSaoJose= {
            "Rua de São José":0,
            "Rua do Raio":0.3,
            "Avenida Dom Joao II":1.0, 
            "Rua do Fujacal":1.3,
            "Rua Joãozinho Azeredo":1.6, 
            "Rua da Igreja":2.2, 
            "Rua da Senra":2.1
        }
        heuristicasGuimaraes= {
            "Rua do Raio":0,
            "Avenida Dom Joao II":0.8, 
            "Rua do Fujacal":0.9,
            "Rua Joãozinho Azeredo":1.4, 
            "Rua da Igreja":1.7, 
            "Rua da Senra":1.7
        }
        heuristicasLanhoso= {
            "Avenida Dom Joao II":0, 
            "Rua do Fujacal":1.5,
            "Rua Joãozinho Azeredo":2.2, 
            "Rua da Igreja":1.6, 
            "Rua da Senra":2.1
        }
        heuristicasBouro= {
            "Rua do Fujacal":0,
            "Rua Joãozinho Azeredo":0.7, 
            "Rua da Igreja":1.5, 
            "Rua da Senra":1
        }
        heuristicasVieiraDoMinho= {
            "Rua Joãozinho Azeredo":0, 
            "Rua da Igreja":2.3, 
            "Rua da Senra":1.3
        }
        heuristicasFamalicao= {
            "Rua da Igreja":0, 
            "Rua da Senra":0.8
        }
        self.heuristicas.append(heuristicasRuadeSãoMartinho)
        self.heuristicas.append(heuristicasRuadaConfeiteira)
        self.heuristicas.append(heuristicasRuadeRedondo)
        self.heuristicas.append(heuristicasCabeceiras)
        self.heuristicas.append(heuristicasCelorico)
        self.heuristicas.append(heuristicaRuaSantaMargarida)
        self.heuristicas.append(heuristicasRuadeSaoJose)
        self.heuristicas.append(heuristicasGuimaraes)
        self.heuristicas.append(heuristicasLanhoso)
        self.heuristicas.append(heuristicasBouro)
        self.heuristicas.append(heuristicasVieiraDoMinho)
        self.heuristicas.append(heuristicasFamalicao)

    def getHeu(self, name, dest):
        for heu in self.heuristicas:
            if heu[name] == 1:
                return heu[dest]
            elif heu[dest] == 0:
                return heu[name]
        return 0

