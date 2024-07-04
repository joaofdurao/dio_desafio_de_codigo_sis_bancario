import os
import json

from models.cliente import Cliente

class ClienteRepository:
    CLIENTE_JSON = os.curdir + '\\repositories\\clientes_repo.json'

    def create_cliente(self, cliente):
        if self.valida_cliente_cpf(cliente.cpf):
            print('CPF já cadastrado.')
            return False
        
        new_cliente = cliente
        new_cliente.id = self.generate_cliente_id()

        try:
            with open(self.CLIENTE_JSON, 'r+') as arquivo:
                try: 
                    clientes = json.load(arquivo)
                except json.JSONDecodeError: 
                    print('Arquivo JSON em branco. Gerando primeiro cliente.')
                    clientes = []
                    
                clientes.append(new_cliente.__dict__)
                arquivo.seek(0)
                json.dump(clientes, arquivo, indent=4)
                arquivo.truncate()
                return True
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False

    def generate_cliente_id(self):
        try:
            with open(self.CLIENTE_JSON, 'r') as arquivo:
                clientes = json.load(arquivo)
                if len(clientes) == 0:
                    return 1
                else:
                    return clientes[-1]['id'] + 1
        except json.decoder.JSONDecodeError:
            return 1
        except Exception as e:
            print(f'Erro no repositorio: {e}')

    def find_cliente_by_id(self, id):
        try:
            with open(self.CLIENTE_JSON, 'r') as arquivo:
                    clientes = json.load(arquivo)
                    for cliente in clientes:
                        if cliente['id'] == id:
                            cliente_result = Cliente(cliente['id'], 
                                                     cliente['nome'], 
                                                     cliente['cpf'], 
                                                     cliente['dt_nasc'], 
                                                     cliente['endereco'])
                            return cliente_result
    
                    raise ValueError('Cliente não encontrado.')
        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')

    def listar_clientes(self):
        try:
            with open(self.CLIENTE_JSON, 'r') as arquivo:
                clientes = json.load(arquivo)
                clientes_list = []
                for cl in clientes:
                    clientes_list.append(Cliente(cl['id'], cl['nome'], cl['cpf'], cl['dt_nasc'], cl['endereco']))
                    return clientes_list

        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')   

    def atualizar_cliente(self, id, cliente):
        try:
            updated_cliente = self.find_cliente_by_id(id)
            if updated_cliente:
                updated_cliente.nome = cliente.nome
                updated_cliente.cpf = cliente.cpf
                updated_cliente.dt_nasc = cliente.dt_nasc
                updated_cliente.endereco = cliente.endereco
                updated_cliente.senha = cliente.senha
            else:
                return False

            with open(self.CLIENTE_JSON, 'r+') as arquivo:
                clientes = json.load(arquivo)
                for c in clientes:
                    if c['id'] == id:
                        c['nome'] = updated_cliente.nome
                        c['cpf'] = updated_cliente.cpf
                        c['dt_nasc'] = updated_cliente.dt_nasc
                        c['endereco'] = updated_cliente.endereco
                        c['senha'] = updated_cliente.senha
                        break

                arquivo.seek(0)
                json.dump(clientes, arquivo, indent=4)
                arquivo.truncate()
                return True
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False
    
    def deletar_cliente(self, id):
        try:
            with open(self.CLIENTE_JSON, 'r+') as arquivo:
                clientes = json.load(arquivo)
                for c in clientes:
                    if c['id'] == id:
                        clientes.remove(c)
                        arquivo.seek(0)
                        json.dump(clientes, arquivo, indent=4)
                        arquivo.truncate()
                        print('Cliente deletado com sucesso.')
                        return True
                return False
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False
    
    def valida_cliente_cpf(self, cpf):
        try:
            with open(self.CLIENTE_JSON, 'r') as arquivo:
                clientes = json.load(arquivo)
                for c in clientes:
                    if c['cpf'] == cpf:
                        return True
                return False
        except Exception:
            return False
        
    def valida_cliente_senha(self, cpf, senha):
        try:
            with open(self.CLIENTE_JSON, 'r') as arquivo:
                clientes = json.load(arquivo)
                for c in clientes:
                    if c['cpf'] == cpf and c['senha'] == senha:
                        return True
                return False
        except Exception:
            return False