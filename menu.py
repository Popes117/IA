import rua as Rua

class Menu:
    def printMenu(self):
        print("[0] Desenha Grafo")
        print("[1] Adicionar Cliente")
        print("[2] Adicionar Estafeta")
        print("[3] Ver Lista estafetas")
        print("[4] Ver Lista Clientes")
        print("[5] Encomendar")
        print("[6] Repetir Encomenda")
        print("[0] Sair")
    def printRuas(self, ruas):
        for i,ruaN in enumerate(ruas):
            print(f"[ {i} ] {ruaN}")