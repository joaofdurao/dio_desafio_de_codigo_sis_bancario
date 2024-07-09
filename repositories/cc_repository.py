import os
import json
from models.conta_corrente import ContaCorrente
from repositories.cliente_repository import ClienteRepository

class CcRepository:
    CC_JSON = os.curdir + '\\repositories\\cc_repo.json'

    def create_conta_corr(self, conta_corr, id_cliente):
        print('Adicionando conta corrente ao repositório.')
        new_conta_corr = conta_corr
        new_conta_corr.id = self._generate_conta_corr_id()
        new_conta_corr.nr_conta = self._generate_conta_corr_nr_conta()
        new_conta_corr.cliente = self._select_conta_corr_cliente(id_cliente)

        new_cc_dict = new_conta_corr.__dict__
        new_cc_dict['cliente'] = new_cc_dict['cliente'].__dict__
        
        try:
            with open(self.CC_JSON, 'r+') as arquivo:
                try:
                    conta_corrs = json.load(arquivo)
                except json.JSONDecodeError:
                    conta_corrs = []

                conta_corrs.append(new_cc_dict)
                arquivo.seek(0)
                json.dump(conta_corrs, arquivo, indent=4)
                arquivo.truncate()
                print('Conta corrente adicionada com sucesso.')
        except Exception as e:
            print(f'Erro no repositório: {e}')

    def find_conta_corr_by_id(self, id):
        try:
            with open(self.CC_JSON, 'r') as arquivo:
                conta_corrs = json.load(arquivo)
                for conta_corr in conta_corrs:
                    if conta_corr['id'] == id:
                        conta_corr_result = ContaCorrente(id =conta_corr['id'], agencia = conta_corr['agencia'], nr_conta = conta_corr['nr_conta'], cliente = conta_corr['cliente'], saldo = conta_corr['saldo'], limite_qnt_saque = conta_corr['limite_qnt_saque'], limite_vlr_saque = conta_corr['limite_vlr_saque'])
                        print(f'Conta corrente encontrada: {conta_corr_result}')
                        return conta_corr_result
        
                return None
        except Exception as e:
            print(f'Erro no repositório: {e}')

    def find_all_contas_corr_by_id_cliente(self, id_cliente):
        try:
            with open(self.CC_JSON, 'r') as arquivo:
                conta_corrs = json.load(arquivo)
                contas_cliente = []
                for conta_corr in conta_corrs:
                    if conta_corr['cliente']['id'] == id_cliente:
                        conta_corr_result = ContaCorrente(id=conta_corr['id'], agencia=conta_corr['agencia'], nr_conta=conta_corr['nr_conta'], cliente=conta_corr['cliente'], saldo=conta_corr['saldo'], limite_qnt_saque=conta_corr['limite_qnt_saque'], limite_vlr_saque=conta_corr['limite_vlr_saque'])
                        contas_cliente.append(conta_corr_result)
                return contas_cliente
        except Exception as e:
            print(f'Erro no repositório: {e}')

    def listar_contas_corr(self):
        with open(self.CC_JSON, 'r') as arquivo:
            conta_corrs = json.load(arquivo)
            conta_corrs_list = []
            for conta_corr in conta_corrs:
                conta_corrs_list.append(ContaCorrente(id =conta_corr['id'], agencia = conta_corr['agencia'], nr_conta = conta_corr['nr_conta'], cliente = conta_corr['cliente'], saldo = conta_corr['saldo'], limite_qnt_saque = conta_corr['limite_qnt_saque'], limite_vlr_saque = conta_corr['limite_vlr_saque']))
            return conta_corrs_list
        print(conta_corrs_list[0])

    def atualizar_conta_corr(self, id, conta_corr):
        try:
            updated_conta_corr = self.find_conta_corr_by_id(id)
            if updated_conta_corr:
                updated_conta_corr.agencia = conta_corr.agencia
                updated_conta_corr.nr_conta = conta_corr.nr_conta
                updated_conta_corr.cliente = conta_corr.cliente
                updated_conta_corr.saldo = conta_corr.saldo
                updated_conta_corr.limite_qnt_saque = conta_corr.limite_qnt_saque
                updated_conta_corr.limite_vlr_saque = conta_corr.limite_vlr_saque

                with open(self.CC_JSON, 'r+') as arquivo:
                    conta_corrs = json.load(arquivo)
                    for c in conta_corrs:
                        if c['id'] == id:
                            c['agencia'] = updated_conta_corr.agencia
                            c['nr_conta'] = updated_conta_corr.nr_conta
                            c['cliente'] = updated_conta_corr.cliente
                            c['saldo'] = updated_conta_corr.saldo
                            c['limite_qnt_saque'] = updated_conta_corr.limite_qnt_saque
                            c['limite_vlr_saque'] = updated_conta_corr.limite_vlr_saque
                            break

                    arquivo.seek(0)
                    json.dump(conta_corrs, arquivo, indent=4)
                    arquivo.truncate()
                    print('Conta corrente atualizada com sucesso.')
            else:
                print('Conta corrente não encontrada.')
        except Exception as e:
            print(f'Erro no repositório: {e}')
    
    def deletar_conta_corr(self, id):
        try:
            with open(self.CC_JSON, 'r+') as arquivo:
                conta_corrs = json.load(arquivo)
                for c in conta_corrs:
                    if c['id'] == id:
                        conta_corrs.remove(c)
                        arquivo.seek(0)
                        json.dump(conta_corrs, arquivo, indent=4)
                        arquivo.truncate()
                        print('Conta corrente deletada com sucesso.')
                        return True
                print('Conta corrente não encontrada.')
                return False
        except Exception as e:
            print(f'Erro no repositório: {e}')
            return False
        

    def _generate_conta_corr_id(self):
        try:
            with open(self.CC_JSON, 'r') as arquivo:
                try:
                    conta_corrs = json.load(arquivo)
                    if len(conta_corrs) == 0:
                        return 1
                    else:
                        return conta_corrs[-1]['id'] + 1
                except json.JSONDecodeError:
                    return 1
        except Exception as e:
            print(f'Erro no repositório: {e}')
            return 1

    def _generate_conta_corr_nr_conta(self):
        try:
            with open(self.CC_JSON, 'r') as arquivo:
                try:
                    conta_corrs = json.load(arquivo)
                    if len(conta_corrs) == 0:
                        return '0001'
                    else:
                        return str(int(conta_corrs[-1]['nr_conta']) + 1).zfill(4)
                except json.JSONDecodeError as e:
                    print(f'Erro no repositório: {e}')
                    return '0001'
        except Exception as e:
            print(f'Erro no repositório: {e}')
            return '0001'

    def _select_conta_corr_cliente(self, id_cliente):
        cliente = ClienteRepository().find_cliente_by_id(id_cliente)
        if cliente:
            return cliente
        else:
            print('Cliente não encontrado.')
            return None
       