from rua import Rua

class Cliente:
    listaClientes = []
    ultimo_id = 0 #incrementa sempre que fizer o registo de um novo

    def __init__(self, id, nome, morada):
        self.id = id
        self.nome = nome
        self.morada = morada
        Cliente.listaClientes.append(self)
        Cliente.ultimo_id = id
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getRua(self):
        return self.morada
    
    def __str__(self):
        return "("+ str(self.id) + ", " + self.nome + ", " + self.morada.getRua() + ")"

    def __repr__(self) -> str:
        return str(self)
    

    def adicionarCliente(nome, morada):
        id = Cliente.ultimo_id + 1
        Cliente(id, nome, morada)
    

def carregarClientes(nome_ficheiro, ruas):
    with open(nome_ficheiro, 'r') as ficheiro:
        for linha in ficheiro:
            campo = linha.strip().split(',')
            id_cliente = int(campo[0])
            nome_cliente = campo[1]
            nome_morada = campo[2]
            
            rua_cliente = None
            for rua in ruas:
                if rua.getNome() == nome_morada:
                    rua_cliente = rua
                    break

            if rua_cliente is not None:
                Cliente(id_cliente, nome_cliente, rua_cliente)
 


def guardarClientes(nome_ficheiro):
    with open(nome_ficheiro, 'w') as ficheiro:
        for cliente in Cliente.listaClientes:
            linha = f"{cliente.getId()},{cliente.getNome()},{cliente.getRua()}\n"
            ficheiro.write(linha)