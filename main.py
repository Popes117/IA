import Graph
import Node
from estafeta import *
from transporte import *
from encomenda import *
from rua import *
import Heu

e1 = Estafeta(1,"João Afonso",4,"Bicicleta")
e2 = Estafeta(2,"Maria Alberta",3.2,"Mota")
e3 = Estafeta(3,"António Moura",2.9,"Bicicleta")
e4 = Estafeta(4,"Francisca Maria",3.7,"Mota")
e5 = Estafeta(5,"José Oliveira",1.9,"Carro")
e6 = Estafeta(6,"Gonçalo Machado",3.7,"Bicicleta")
e7 = Estafeta(7,"Maria João",4.2,"Bicicleta")
e8 = Estafeta(8,"Pedro Lopes",3.4,"Carro")
e9 = Estafeta(9,"Marta Rodrigues",4.5,"Carro")

heuristicas = Heu()
heuristicas.fillHeuristicas() #mudar esta funcao

t1 = Transporte("Bicicleta", 5, 10)
t2 = Transporte("Mota", 20, 35)
t3 = Transporte("Carro", 100, 50)


rua1 = Rua("Rua da Confeiteira", "Palmeira")
rua2 = Rua("Rua de Redondo", "Adaufe")
rua3 = Rua("Rua de São Martinho", "Dume")
rua4 = Rua("Rua 5 de Outubro", "Real")
rua5 = Rua("Rua da Universidade", "Gualtar")
rua6 = Rua("Rua Santa Margarida", "São Vicente")
rua7 = Rua("Rua de São José", "São Vitor")
rua8 = Rua("Rua do Raio", "São Vitor")
rua9 = Rua("Avenida Dom Joao II", "Nogueiró")
rua10 = Rua("Rua do Fujacal", "São Lazaro")
rua11 = Rua("Rua Joãozinho Azeredo", "Maximinos")
rua12 = Rua("Rua da Igreja", "Nogueira")
rua13 = Rua("Rua da Senra", "Lamacães")


g = Graph()
#deve ser aqui substituido por ruax ???
g.add_edge("Rua da Confeiteira", "Rua de Redondo", 10) #rua1, rua2
g.add_edge("Rua da Confeiteira", "Rua de São Martinho", 17) #rua1, rua3
g.add_edge("Rua da Confeiteira", "Rua 5 de Outubro", 18) #rua1, rua4
g.add_edge("Rua da Confeiteira", "Rua Santa Margarida", 10) #rua1, rua6
g.add_edge("Rua de Redondo", "Rua da Universidade", 27) #rua2, rua5
g.add_edge("Rua de São Martinho","Rua 5 de Outubro", 5) #rua3, rua4
g.add_edge("Rua de São Martinho", "Rua Santa Margarida", 15) #rua3, rua6
g.add_edge("Rua de São Martinho", "Rua de São José", 20) #rua3, rua6
g.add_edge("Rua 5 de Outubro", "Rua Santa Margarida", 17) #rua4, rua6
g.add_edge("Rua 5 de Outubro", "Rua de São José",25) #rua4, rua7
g.add_edge("Rua 5 de Outubro", "Rua Joãozinho Azeredo", 20) #rua4, rua11
g.add_edge("Rua da Universidade", "Rua Santa Margarida", 10) #rua5, rua6
g.add_edge("Rua da Universidade", "Rua de São José", 10) #rua5, rua7
g.add_edge("Rua da Universidade", "Rua do Raio", 10) #rua5, rua8
g.add_edge("Rua da Universidade", "Avenida Dom Joao II", 10) #rua5, rua9
g.add_edge("Rua Santa Margarida", "Rua de São José", 10) #rua6, rua7
g.add_edge("Rua Santa Margarida", "Rua do Raio", 10)#rua6, rua8
g.add_edge("Rua Santa Margarida", "Rua do Fujacal", 10)#rua6, rua10
g.add_edge("Rua Santa Margarida", "Rua Joãozinho Azeredo",10) #rua6, rua11
g.add_edge("Rua de São José", "Rua do Raio", 5) #rua7, rua8
g.add_edge("Rua de São José", "Avenida Dom Joao II" , 10) #rua7, rua9
g.add_edge("Rua de São José", "Rua da Igreja", 10) #rua7, rua12
g.add_edge("Rua de São José", "Rua da Senra", 10) #rua7, rua13
g.add_edge("Rua do Raio", "Rua do Fujacal", 10) #rua8, rua10
g.add_edge("Rua do Raio", "Rua da Senra", 10) #rua8, rua13
g.add_edge("Avenida Dom Joao II", "Rua da Igreja", 10) #rua9, rua12
g.add_edge("Avenida Dom Joao II", "Rua da Senra", 10) #rua9, rua13
g.add_edge("Rua do Fujacal", "Rua Joãozinho Azeredo", 10) #rua10, rua11
g.add_edge("Rua do Fujacal", "Rua da Igreja", 10) #rua10, #rua12
g.add_edge("Rua da Igreja", "Rua da Senra", 10) #rua12, rua13



#g.add_edge("Braga", "Amares", 15)#
#g.add_edge("Braga", "Póvoa de Lanhoso", 16)#
#g.add_edge("Braga", "Vila Verde", 17)#
#g.add_edge("Braga", "Barcelos", 27)#
#g.add_edge("Braga", "Vila Nova de Famalicão", 25)#
#g.add_edge("Braga", "Guimarães", 22)#
#g.add_edge("Amares", "Vila Verde", 13)#
#g.add_edge("Amares", "Terras de Bouro", 16)#
#g.add_edge("Amares", "Póvoa de Lanhoso", 14)#
#g.add_edge("Terras de Bouro", "Vieira do Minho", 25)#
#g.add_edge("Terras de Bouro", "Vila Verde", 25)#
#g.add_edge("Vieira do Minho", "Fafe", 30)#
#g.add_edge("Vieira do Minho", "Póvoa de Lanhoso", 16)#
#g.add_edge("Vieira do Minho", "Cabeceiras de Basto", 26)#
#g.add_edge("Cabeceiras de Basto", "Fafe", 29)#
#g.add_edge("Cabeceiras de Basto", "Celorico de Basto", 25)#
#g.add_edge("Celorico de Basto", "Fafe", 26)#
#g.add_edge("Fafe", "Póvoa de Lanhoso", 29)#
#g.add_edge("Fafe", "Guimarães", 15)#
#g.add_edge("Vizela", "Guimarães", 18)#
#g.add_edge("Guimarães", "Vila Nova de Famalicão", 25)#
#g.add_edge("Guimarães", "Póvoa de Lanhoso", 24)#
#g.add_edge("Barcelos", "Vila Nova de Famalicão",22)#
#g.add_edge("Barcelos", "Esposende", 16)#
#g.add_edge("Barcelos", "Vila Verde", 26)#
#g.add_edge("Vila Verde", "Amares", 13)#
