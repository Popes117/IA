import Graph
import Node
import Estafeta
import Heu

e1 = Estafeta("João Afonso",3,"Barcelos","Bicicleta")
e2 = Estafeta("Maria Alberta",3,"Póvoa de Lanhoso","Mota")
e3 = Estafeta("António Moura",3,"Vila Nova de Famalicão","Bicicleta")
e4 = Estafeta("Francisca Maria",3,"Guimarães","Mota")
e5 = Estafeta("José Oliveira",3,"Vila Verde","Carro")
e6 = Estafeta("Gonçalo Machado",3,"Vizela","Bicicleta")
e7 = Estafeta("Maria João",3,"Braga","Bicicleta")
e8 = Estafeta("Pedro Lopes",3,"Braga","Carro")
e9 = Estafeta("Marta Rodrigues",3,"Esposende","Carro")

heuristicas = Heu()
heuristicas.fillHeuristicas()



g = Graph()
g.add_edge("Braga", "Amares", 15)#
g.add_edge("Braga", "Póvoa de Lanhoso", 16)#
g.add_edge("Braga", "Vila Verde", 17)#
g.add_edge("Braga", "Barcelos", 27)#
g.add_edge("Braga", "Vila Nova de Famalicão", 25)#
g.add_edge("Braga", "Guimarães", 22)#
g.add_edge("Amares", "Vila Verde", 13)#
g.add_edge("Amares", "Terras de Bouro", 16)#
g.add_edge("Amares", "Póvoa de Lanhoso", 14)#
g.add_edge("Terras de Bouro", "Vieira do Minho", 25)#
g.add_edge("Terras de Bouro", "Vila Verde", 25)#
g.add_edge("Vieira do Minho", "Fafe", 30)#
g.add_edge("Vieira do Minho", "Póvoa de Lanhoso", 16)#
g.add_edge("Vieira do Minho", "Cabeceiras de Basto", 26)#
g.add_edge("Cabeceiras de Basto", "Fafe", 29)#
g.add_edge("Cabeceiras de Basto", "Celorico de Basto", 25)#
g.add_edge("Celorico de Basto", "Fafe", 26)#
g.add_edge("Fafe", "Póvoa de Lanhoso", 29)#
g.add_edge("Fafe", "Guimarães", 15)#
g.add_edge("Vizela", "Guimarães", 18)#
g.add_edge("Guimarães", "Vila Nova de Famalicão", 25)#
g.add_edge("Guimarães", "Póvoa de Lanhoso", 24)#
g.add_edge("Barcelos", "Vila Nova de Famalicão",22)#
g.add_edge("Barcelos", "Esposende", 16)#
g.add_edge("Barcelos", "Vila Verde", 26)#
g.add_edge("Vila Verde", "Amares", 13)#





# Amares,
# Barcelos,
# Braga,
# Cabeceiras de Basto,
# Celorico de Basto,
# Esposende,
# Fafe,
# Guimarães,
# Póvoa de Lanhoso, 
# Terras de Bouro,
# Vieira do Minho, 
# Vila Nova de Famalicão, 
# Vila Verde 
# Vizela
