from Graph import Grafo
from estafeta import *
from transporte import *
from encomenda import *
from rua import *
from cliente import *
from Heu import Heu
from menu import *

""" Zé: Corrigir os algoritmos(Greedy) e testar os outros(BFS, DFS, A*)
        Testar a decisao de transporte

    Marta: Implementar serviços (entregas com varias encomendas)

""" 

def main():
    listEncomendas = list()
    idEncomenda = 0

    heuristicas = Heu()
    heuristicas.fillHeuristicas() #mudar esta funcao


    t1 = Transporte("Bicicleta", 5, 10)
    t2 = Transporte("Mota", 20, 35)
    t3 = Transporte("Carro", 100, 50)

    rua0 = Rua("Central", "Sao Lazaro") #Central da Health Planet
    rua1 = Rua("Rua da Confeiteira", "Palmeira")
    rua2 = Rua("Rua de Redondo", "Adaufe")
    rua3 = Rua("Rua de Sao Martinho", "Dume")
    rua4 = Rua("Rua 5 de Outubro", "Real")
    rua5 = Rua("Rua da Universidade", "Gualtar")
    rua6 = Rua("Rua Santa Margarida", "Sao Vicente")
    rua7 = Rua("Rua de Sao Jose", "Sao Vitor")
    rua8 = Rua("Rua do Raio", "Sao Vitor")
    rua9 = Rua("Avenida Dom Joao II", "Nogueiro")
    rua10 = Rua("Rua do Fujacal", "Sao Lazaro")
    rua11 = Rua("Rua Joaozinho Azeredo", "Maximinos")
    rua12 = Rua("Rua da Igreja", "Nogueira")
    rua13 = Rua("Rua da Senra", "Lamacaes")
    lista_ruas = [rua1,rua2,rua3,rua4,rua5,rua6,rua7,rua8,rua9,rua10,rua11,rua12,rua13]


    g = Grafo(heuristicas)
    g.add_edge(rua0, rua3, 3.7)
    g.add_edge(rua0, rua4, 3.3)
    g.add_edge(rua0, rua5, 2.2)
    g.add_edge(rua0, rua6, 0.5)
    g.add_edge(rua0, rua8, 0.3)
    g.add_edge(rua0, rua9, 2.9)
    g.add_edge(rua0, rua10, 2.3)
    g.add_edge(rua0, rua11, 1.8)
    g.add_edge(rua0, rua13, 3.1)
    g.add_edge(rua1, rua3, 2.8) 
    g.add_edge(rua1, rua2, 2.8) 
    g.add_edge(rua1, rua4, 1.7) 
    g.add_edge(rua1, rua6, 3.6) 
    g.add_edge(rua2, rua5, 1.5) 
    g.add_edge(rua3, rua4, 1.2) 
    g.add_edge(rua3, rua6, 1.5) 
    g.add_edge(rua3, rua7, 3.0) 
    g.add_edge(rua4, rua6, 1.3) 
    g.add_edge(rua4, rua7, 2.0) 
    g.add_edge(rua4, rua11, 1.9)
    g.add_edge(rua5, rua7, 1.5) 
    g.add_edge(rua5, rua8, 1.7) 
    g.add_edge(rua5, rua9, 1.6) 
    g.add_edge(rua6, rua7, 1.0) 
    g.add_edge(rua6, rua8, 0.8)
    g.add_edge(rua6, rua10, 1.3)
    g.add_edge(rua6, rua11, 1.1)
    g.add_edge(rua7, rua8, 0.5)
    g.add_edge(rua7, rua9 , 1.2)
    g.add_edge(rua8, rua9 , 1.0)
    g.add_edge(rua7, rua12, 2.9) 
    g.add_edge(rua7, rua13, 3.5) 
    g.add_edge(rua8, rua10, 1.4) 
    g.add_edge(rua8, rua13, 2.7) 
    g.add_edge(rua9, rua12, 2.0) 
    g.add_edge(rua9, rua13, 2.9) 
    g.add_edge(rua10, rua11, 1.3) 
    g.add_edge(rua10, rua12, 1.9)
    g.add_edge(rua12, rua13, 0.9) 


    #Leitura dos ficheiros .txt com os estafetas e clientes
    carregarEstafetas('./estafetas.txt')
    carregarClientes('./clientes.txt', lista_ruas)
    carregarEstafetas('./encomendas.txt')


    #Interface
    m = Menu()
    print("\n******** BEM VINDO AO HEALTH PLANET ********\n")

    userInput = -1
    while userInput != 0:

        m.printMenu()
        userInput = int(input("Escolha opcao: "))

        #Opcoes Cliente
        if userInput == 1: 
            opcao1 = -1
            while opcao1 != 0:
                m.menu_cliente()
                opcao1 = int(input("Escolha opcao: "))


                #adicionar novo cliente - melhorar isto
                if opcao1 == 1: 
                    clienteNome = input("Escolha Nome: ")
                    
                    m.printRuas(lista_ruas)
                    clienteRua = int(input("Escolha Rua (insira o número da rua): "))
                    if 1 <= clienteRua < len(lista_ruas):
                        rua_escolhida = lista_ruas[clienteRua - 1]
                        print("Rua escolhida: ", rua_escolhida)
                    
                        Cliente.adicionarCliente(clienteNome, rua_escolhida)
                        print("Cliente Criado.")
                
                    else:
                        print("Índice fora dos limites da lista. Escolha inválida.")


                #Imprimir Lista de Clientes Registados
                if opcao1 == 2:
                    print("\n**** Clientes ****")
                    for cliente in Cliente.listaClientes:
                        print(str(cliente))


        #Opcoes Estafeta
        if userInput == 2:
            opcao2 = -1
            while opcao2 != 0:
                m.menu_estafetas()
                opcao2 = int(input("Escolha opcao: "))
                
                #adicionar novo estafeta
                if opcao2 == 1: 
                    estafetaNome = input("Escolha nome:")
                    Estafeta.adicionarEstafeta(estafetaNome,0,0)

                
                #Imprimir Lista de Estafetas Registados
                if opcao2 == 2:
                    print("\n**** Estafetas ****")
                    for estafeta in Estafeta.listaEstafeta:
                        print(str(estafeta))


        if userInput == 3:
            encomendaIdC = int(input("Id Cliente: "))
            peso = float(input("Peso da Encomenda: "))
            volume = float(input("Volume da encomenda(em centímetros cúbicos): "))
            tempoLimite = int(input("Hora limite de entrega(minutos): "))
            morada = rua0
            m.printAlgoritmos()
            algoritmo = int(input("Escolha o algoritmo que deseja utilizar: "))
            for estafeta in Estafeta.listaEstafeta:
                print(str(estafeta))
            estafeta = int(input("Escolha Estafeta: "))
            
            rua = None
            for cliente in Cliente.listaClientes:
                if cliente.getId() == encomendaIdC:
                    encomenda = Encomenda(idEncomenda,encomendaIdC,estafeta,peso,volume,tempoLimite,cliente.getRua())
                    idEncomenda += 1
                    listEncomendas.append(encomenda)
                    rua = cliente.getRua()
                    break
            print(rua)


            (path, custo, visitados) = (None,None,None)
            if algoritmo == 1:
                path, custo, visitados = g.procura_aStar(rua,morada)
            elif algoritmo == 2:
                (path, custo, visitados) = g.greedy(rua,morada)
            elif algoritmo == 3:
                (path, custo, visitados) = g.procura_BFS(rua,morada)
            elif algoritmo == 4:
                (path, custo, visitados) = g.procura_DFS(rua,morada)
            else:
                print("Input inválido")
            if path != None:
                estafetaEsc = Estafeta.listaEstafeta[estafeta-1]
                trans,tempoGasto = estafetaEsc.chooseTransport(peso,custo,tempoLimite)
                print(f"Caminho escolhido: {path}")
                print(f"Nodos Visitados: {visitados}")
                print(f"Transporte Escolhido: {trans}")

                aval = 5
                estafeta_escolhido = Estafeta.listaEstafeta[estafeta-1]
                if tempoGasto <= tempoLimite:
                    print(f"Tempo de entrega: {tempoGasto}")
                    print("Avaliação dada: 5")
                    estafeta_escolhido.updateAvaliacao(aval)
                    pass
                else:
                    percentAtraso = (tempoGasto - tempoLimite)/tempoLimite
                    aval = avalia(1-percentAtraso)
                    estafeta_escolhido.updateAvaliacao(aval)

                

            else: 
                print("Caminho nao encontrado.")
                
            

                      
        #Imprimir Ruas
        if userInput == 5: 
            #print(g.imprime_aresta()) #imprime arestas - trocar!
            print(rua0.getRua())
            for rua in lista_ruas:
                print(rua.getRua())

        #Desenhar Grafo
        if userInput == 6:
            g.desenha()
            
        #Guardar alteracões
        if userInput == 7:
            guardarEstafetas('./estafetas.txt')
            guardarClientes('./clientes.txt')
            print("\nAlteracões Guardadas!\n")


        #acrescentar aqui cenas...
    
                
        if userInput == 0: #Sair
            print("\nA sair...")

        else:
            print("Input inválido.\n")





if __name__ == "__main__":
    main()
