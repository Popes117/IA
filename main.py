from Graph import Grafo
from estafeta import *
from transporte import *
from encomenda import *
from rua import *
from cliente import *
from Heu import Heu
from menu import *
import random


def preço(peso, volume, transporte):
        if transporte == "Bicicleta":
            return 1 + peso*volume/100
        elif transporte == "Mota":
            return 3 + 2*peso*volume/100
        else:
            return 5 + 4*peso*volume/100

def main():
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
    g.add_edge(rua0, rua10, 2.3)
    g.add_edge(rua0, rua12, 1.5)
    g.add_edge(rua0, rua13, 0.4)
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


    #Leitura dos ficheiros .txt com os estafetas, clientes e encomendas pré feitas
    carregarEstafetas('./estafetas.txt')
    carregarClientes('./clientes.txt', lista_ruas)
    carregarEncomendas('./encomendas.txt')

    #encomendasAgrupadas => {Data : [{[encomendas],pesototaldasencomendas}]}
    #dicionario cuja chave são as suas datas. Para cada data terá listas de grupos. estes são separados por pesos.
    #por isso cada lista terá um tuplo com sua lista de encomendas e o peso total das encomendas nessa mesma lista
    encomendasAgrupadas = agruparEncomendas()
    

    #Interface
    m = Menu()
    print("\n******** BEM VINDO AO HEALTH PLANET ********")

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


                #Adicionar novo cliente
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
        elif userInput == 2:
            opcao2 = -1
            while opcao2 != 0:
                m.menu_estafetas()
                opcao2 = int(input("Escolha opcao: "))
                
                #Adicionar novo estafeta
                if opcao2 == 1: 
                    estafetaNome = input("Escolha nome:")
                    Estafeta.adicionarEstafeta(estafetaNome,0,0)
                
                #Imprimir Lista de Estafetas Registados
                if opcao2 == 2:
                    print("\n**** Estafetas ****")
                    for estafeta in Estafeta.listaEstafeta:
                        print(str(estafeta))
                
        #Registar Nova Encomenda
        elif userInput == 3:
            print("\n****** Nova Encomenda ******")
            #Informações da Encomenda
            encomendaIdC = int(input("Id Cliente: "))
            peso = float(input("Peso da Encomenda: "))
            if peso > 100:
                print("Peso não suportado")
            else:
                volume = float(input("Volume da encomenda(em centímetros cúbicos): "))
                tempoLimite = int(input("Hora limite de entrega(minutos): "))
                dataEntrega = input("Data de Entrega (DD/MM/AAAA): ")

            #Adicionar Encomenda as encomendas já existentes
                rua = None
                for cliente in Cliente.listaClientes:
                    if cliente.getId() == encomendaIdC:
                        rua = cliente.getRua()
                        idEncomenda = Encomenda.adicionarEncomenda(encomendaIdC,peso,volume,tempoLimite,rua,dataEntrega)
                        encomendasAgrupadas = agruparEncomendas()
                        break
            

                #Permite visualizar um plano inicial do percurso da sua encomenda
                visualizar = input("Visualizar o seu percurso inicial apenas para esta encomenda? (y/n): ")
                if visualizar == "y":
                
                    m.printAlgoritmos()
                    algoritmo = int(input("Escolha o algoritmo que deseja utilizar: "))
                    for estafeta in Estafeta.listaEstafeta:
                        print(str(estafeta))
                    estafeta = int(input("Escolha Estafeta: "))

                #Procura com algoritmo pedido
                    (path, custo, visitados) = (None,None,None)
                    if algoritmo == 1:
                        path, custo, visitados = g.procura_aStar(rua0,rua)
                    elif algoritmo == 2:
                        (path, custo, visitados) = g.procura_greedy(rua0,rua)
                    elif algoritmo == 3:
                        (path, custo, visitados) = g.procura_BFS(rua0,rua)
                    elif algoritmo == 4:
                        (path, custo, visitados) = g.procura_DFS(rua0,rua)
                    elif algoritmo == 5:
                        (path, custo, visitados) = g.uniform_cost_search(rua0,rua)
                    elif algoritmo == 6:
                        (path, custo, visitados) = g.melhorCircuito(rua0,rua)
                    else:
                        print("Input inválido")

                    if path != None:
                        estafetaEsc = Estafeta.listaEstafeta[estafeta-1]
                        trans,tempoGasto = estafetaEsc.chooseTransport(peso,custo,tempoLimite)
                        print(f"\nCaminho escolhido: {path}")
                        print(f"Distancia Percorrida: {custo}")
                        print(f"Nodos Visitados: {visitados}")
                        print(f"Transporte Escolhido: {trans}")
                        print(f"Tempo de Entrega: {tempoGasto}")

                        print(f"Preço da Encomenda:{preço(peso, volume, trans): .2f}")

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

                    print("\nID da Nova Encomenda: ", idEncomenda, "\n")
                else:
                    print("\nID da Nova Encomenda: ", idEncomenda, "\n")



 
        #Visualizar Percursos - permite ver o percurso de uma determinada encomenda
        elif userInput == 4:
            encomendaId = int(input("Insira o id da encomenda: ")) 
            if 1 <= encomendaId <= Encomenda.ultimo_id:

                encProcura = Encomenda.listaEncomendas[encomendaId]
                listaEncomendas = encomendasAgrupadas[encProcura.getData()]

                for grupo in listaEncomendas:
                    if encomendaId in grupo['encomendas']:
                        listaServico = grupo['encomendas']
                        pesoServico = grupo['peso']
                        break 

                
                flag = 0
                #Se a lista obtida tiver apenas 1 unico elemento, irá usar os algoritmos de procura simples
                if len(listaServico) == 1:
                    caminho = encProcura.getMorada()
                    tempoLimite = encProcura.getPrazo()
                    flag = 1

                #se tiver mais que 1 usa os complexos
                else:
                    caminho = []
                    #Ordena por ordem dos prazos das encomendas
                    encomendas_ordenadas = sorted(listaServico, key=lambda encomenda_id: Encomenda.listaEncomendas[encomenda_id].prazo_limite)
                    tempoLimite = encomendas_ordenadas[-1] #tempo limite a tentar cumprir é o maior de todas as encomendas
                    #coloca as ruas numa lista
                    for i in encomendas_ordenadas:
                        caminho.append(Encomenda.listaEncomendas[i].getMorada())
                        
                print(caminho)
                m.printAlgoritmos()
                algoritmo = int(input("Escolha o algoritmo que deseja utilizar: "))

                (path, custo, visitados) = (None,None,None)
                #Procura Simples - caso a lista só tenha uma unica encomenda
                if flag == 1:
                    if algoritmo == 1: 
                        path, custo, visitados = g.procura_aStar(rua0,caminho)
                    elif algoritmo == 2:
                        (path, custo, visitados) = g.procura_greedy(rua0,caminho)
                    elif algoritmo == 3:
                        (path, custo, visitados) = g.procura_BFS(rua0,caminho)
                    elif algoritmo == 4:
                        (path, custo, visitados) = g.procura_DFS(rua0,caminho)
                    elif algoritmo == 5:
                        (path, custo, visitados) = g.uniform_cost_search(rua0,rua)
                    elif algoritmo == 6:
                        (path, custo, visitados) = g.melhorCircuito(rua0,rua)
                    else:
                        print("Input inválido")

                #Procura Complexa - caso a lista tenha mais que uma encomenda
                else:
                    if algoritmo == 1: 
                        path, custo, visitados = g.procura_aStar_Varias(rua0,caminho)
                    elif algoritmo == 2:
                        (path, custo, visitados) = g.procura_greedy_Varias(rua0,caminho)
                    elif algoritmo == 3:
                        (path, custo, visitados) = g.procura_BFS_Varias(rua0,caminho)
                    elif algoritmo == 4:
                        (path, custo, visitados) = g.procura_DFS_Varias(rua0,caminho)
                    elif algoritmo == 5:
                        (path, custo, visitados) = g.procura_Custo_uni_varias(rua0,caminho)
                    else:
                        print("Input inválido")


                estafeta_escolhido = Estafeta.listaEstafeta[random.randint(0,Estafeta.ultimo_id - 1)]
                if path != None:
                        trans,tempoGasto = estafeta_escolhido.chooseTransport(pesoServico,custo,tempoLimite)
                        print(f"\nCaminho escolhido: {path}")
                        print(f"Distancia Percorrida:{custo: .2f}")
                        print(f"Nodos Visitados: {visitados}")
                        print(f"Transporte Escolhido: {trans}")
                        
                        peso = encProcura.getPeso()
                        volume = encProcura.getVolume()
                        print(f"Preço da Encomenda:{preço(peso, volume, trans): .2f}")

                        #Avalia o Estafeta
                        aval = 5
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
                print("Encomenda não existe!")

        #Imprimir Ruas
        elif userInput == 5: 
            print("**** Ruas ****")
            print(rua0.getRua())
            for rua in lista_ruas:
                print(rua.getRua())

        #Ver Caminhos
        elif userInput == 6:
            print(g.imprime_aresta())

        #Desenhar Grafo
        elif userInput == 7:
            print("A gerar grafo...")
            g.desenha()
            
        #Guardar alteracões
        elif userInput == 8:
            guardarEstafetas('./estafetas.txt')
            guardarClientes('./clientes.txt')
            guardarEncomendas('./encomendas.txt')
            print("\nAlteracões Guardadas!\n")
    
         #Sair
        elif userInput == 0:
            print("\nA sair...")

        else:
            print("Input inválido.\n")





if __name__ == "__main__":
    main()
