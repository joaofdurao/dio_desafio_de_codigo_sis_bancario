from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository as CRepo

class ClienteController:

    def criar_cliente(self, nome_cliente, cpf_cliente, dt_nasc_cliente, logradouro_cliente, nr_cliente, bairro_cliente, cidade_cliente, estado_cliente, senha_cliente):
        endereco_cliente = f'{logradouro_cliente},{nr_cliente},{bairro_cliente},{cidade_cliente}/{estado_cliente}'
        cliente = Cliente(nome = nome_cliente, cpf = cpf_cliente, dt_nasc = dt_nasc_cliente, endereco = endereco_cliente, senha = senha_cliente)
        
        try: 
            CRepo.create_cliente(cliente)
            return True  
        except Exception:
            return False

    def encontrar_cliente(self, cliente_id):
        try:
            cliente = CRepo.find_cliente_by_id(cliente_id)
            cliente_dict = cliente.__dict__
            return cliente_dict
        except Exception:
            return False

    def listar_clientes(self):
        

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