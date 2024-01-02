from rua import *

class Menu:
    def printMenu(self):
        print("[1] Opções Cliente")
        print("[2] Opções Estafeta")
        print("[3] Encomendar")
        #print("[4] Repetir Encomenda")
        print("[4] Registar Nova Encomenda")
        print("[8] Visualizar Percursos")
        print("[5] Ver Ruas")
        print("[6] Desenhar Mapa")
        print("[7] Guardar Alterações (caso tenha realizado novos registos)")
        print("[0] Sair")


    def printRuas(self, ruas):
        for i,ruaN in enumerate(ruas):
            print(f"[ {i + 1} ] {ruaN}")


    def menu_cliente(self): #pode passar para a lista normal
        print("\n******** Opções Cliente ********")
        print("[1] Novo Cliente")
        print("[2] Ver Lista Clientes")
        print("[0] Voltar ao menu principal")


    def menu_estafetas(self):
        print("\n******** Opções Estafeta ********")
        print("[1] Novo Estafeta")
        print("[2] Ver Lista Estafetas")
        print("[0] Voltar ao menu principal")


    def menu_encomendas(self):
        print("\n******** Encomendar ********")
        print("[1] Registar Nova Encomenda") #??
        print("[2] Gerar Circuito de Entrega") #meter aqui os varios tipos de algoritmos
        print("[3] Realizar Encomendas") #recebe uma ou varias encomendas

    def printAlgoritmos(self):
        print("[1] A*")
        print("[2] Greedy")
        print("[3] BFS")
        print("[4] DFS")
        print("[5] Cost Uniform Search")
        print("[6] Melhor Circuito")

    def printTransporte(self, trans):
        if trans == 1:
            print("Bicicleta")
        if trans == 2:
            print("Mota")
        if trans == 3:
            print("Carro")
