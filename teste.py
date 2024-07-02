from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository

c1 = Cliente(nome='Lucas', cpf='123.456.789-00', dt_nasc='2000-11-21', endereco='Rua 1, 123, Bairro 1, Cidade 1/UF')

repo = ClienteRepository()

# repo.create_cliente(c1)
# repo.find_cliente_by_id(2)
# repo.listar_clientes()
# repo.atualizar_cliente(2, c1)
repo.deletar_cliente(4)