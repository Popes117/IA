from rua import *

class Menu:
    def printMenu(self):
        print("\n[1] Opções Cliente")
        print("[2] Opções Estafeta")
        #print("[3] Encomendar")
        #print("[4] Repetir Encomenda")
        print("[3] Registar Nova Encomenda")
        print("[4] Visualizar Percursos Das Encomendas")
        print("[5] Ver Ruas")
        print("[6] Ver Caminhos")
        print("[7] Desenhar Mapa")
        print("[8] Guardar Alterações (caso tenha realizado novos registos)")
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
