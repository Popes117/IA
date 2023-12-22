class Encomenda:
    def __init__(self, id, id_cliente, peso, volume, prazo_limite, morada_entrega):
        self.id = id
        self.id_cliente = id_cliente
        self.peso = peso
        self.volume = volume
        self.prazo_limite = prazo_limite
        self.morada_entrega = morada_entrega