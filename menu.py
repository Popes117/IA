import rua as Rua

class Menu:
    def printMenu(self):
        print("[1] Opções Cliente")
        print("[2] Opções Estafeta")
        print("[3] Encomendar")
        print("[4] Repetir Encomenda")
        print("[5] Ver Ruas")
        print("[6] Desenhar Mapa")
        print("[7] Guardar Alterações (caso tenha realizado novos registos)")
        print("[0] Sair")


    def printRuas(self, ruas):
        for i,ruaN in enumerate(ruas):
            print(f"[ {i} ] {ruaN}")


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

