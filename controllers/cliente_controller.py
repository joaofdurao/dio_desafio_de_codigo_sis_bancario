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
        try:
            clientes = CRepo.list_clientes()
            clientes_dict = []
            for i in clientes:
                clientes_dict.append(i.__dict__)
            return clientes_dict
        except Exception:
            return False

    def atualizar_cliente(self, id_cliente, nome_cliente = None, cpf_cliente = None, dt_nasc_cliente = None, logradouro_cliente = None, nr_cliente = None, bairro_cliente = None, cidade_cliente = None, estado_cliente = None, senha_cliente = None):
        try:
            endereco_cliente = f'{logradouro_cliente},{nr_cliente},{bairro_cliente},{cidade_cliente}/{estado_cliente}'
            cliente = Cliente(id = id_cliente, nome = nome_cliente, cpf = cpf_cliente, dt_nasc = dt_nasc_cliente, endereco = endereco_cliente, senha = senha_cliente)
            CRepo.update_cliente(cliente)
            return True
        except Exception:
            return False

    def deletar_cliente(self, id_cliente):
        try:
            CRepo.delete_cliente(id_cliente)
            return True
        except Exception:
            return False