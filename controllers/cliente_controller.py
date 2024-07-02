from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository

class ClienteController:

    def criar_cliente(self, nome=None, cpf=None, dt_nasc=None, logradouro=None, nr=None, bairro=None, cidade=None, estado=None):
        endereco = f'{logradouro},{nr},{bairro},{cidade}/{estado}'
        cliente = Cliente(nome = nome, cpf = cpf, dt_nasc = dt_nasc, endereco = endereco)
        
        try: 
            ClienteRepository().create_cliente(cliente)
            return True  
        except Exception:
            return False

    def obter_cliente(self, nome=None, cpf=None, dt_nasc=None, endereco=None):
        
        
        
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