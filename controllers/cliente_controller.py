from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository

class ClienteController:
    def __init__(self):
        self.cliente = Cliente()
        self.repo = ClienteRepository()

    def criar_cliente(self, nome, email):
        cliente = {"nome": nome, "email": email}
        self.clientes.append(cliente)
        return cliente

    def obter_cliente(self, nome):
        for cliente in self.clientes:
            if cliente["nome"] == nome:
                return cliente
        return None

    def atualizar_cliente(self, nome, novo_email):
        cliente = self.obter_cliente(nome)
        if cliente:
            cliente["email"] = novo_email
            return True
        return False

    def deletar_cliente(self, nome):
        cliente = self.obter_cliente(nome)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False