import os
import json

from models.transacao import Transacao

class TransacaoRepository:
    TRANSACAO_JSON = os.curdir + '\\repositories\\transacoes_repo.json'

    def create_transacao(self, transacao):
        new_transacao = transacao
        new_transacao.id = self._generate_transacao_id()

        try:
            with open(self.TRANSACAO_JSON, 'r+') as arquivo:
                try: 
                    transacoes = json.load(arquivo)
                except json.JSONDecodeError: 
                    print('Arquivo JSON em branco. Gerando primeira transacao.')
                    transacoes = []
                    
                transacoes.append(new_transacao.__dict__)
                arquivo.seek(0)
                json.dump(transacoes, arquivo, indent=4)
                arquivo.truncate()
                return True
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False

    def find_transacao_by_id(self, id):
        try:
            with open(self.TRANSACAO_JSON, 'r') as arquivo:
                    transacoes = json.load(arquivo)
                    for transacao in transacoes:
                        if transacao['id'] == id:
                            transacao_result = Transacao(transacao['id'], 
                                                     transacao['valor'], 
                                                     transacao['data'], 
                                                     transacao['tipo'], 
                                                     transacao['conta'], 
                                                     transacao['cliente'])
                            return transacao_result
                    
                    raise ValueError('Transacao não encontrada.')
        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')
    
    def list_transacoes(self):
        try:
            with open(self.TRANSACAO_JSON, 'r') as arquivo:
                transacoes = json.load(arquivo)
                transacoes_list = []
                for transacao in transacoes:
                    transacao_obj = Transacao(transacao['id'], 
                                              transacao['valor'], 
                                              transacao['data'], 
                                              transacao['tipo'], 
                                              transacao['conta'], 
                                              transacao['cliente'])
                    transacoes_list.append(transacao_obj)
                return transacoes_list
        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')
    
    def update_transacao(self, transacao):
        try:
            with open(self.TRANSACAO_JSON, 'r+') as arquivo:
                transacoes = json.load(arquivo)
                for i, t in enumerate(transacoes):
                    if t['id'] == transacao.id:
                        transacoes[i] = transacao.__dict__
                        arquivo.seek(0)
                        json.dump(transacoes, arquivo, indent=4)
                        arquivo.truncate()
                        return True
                raise ValueError('Transacao não encontrada.')
        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False
    
    def delete_transacao(self, id):
        try:
            with open(self.TRANSACAO_JSON, 'r+') as arquivo:
                transacoes = json.load(arquivo)
                for i, t in enumerate(transacoes):
                    if t['id'] == id:
                        del transacoes[i]
                        arquivo.seek(0)
                        json.dump(transacoes, arquivo, indent=4)
                        arquivo.truncate()
                        return True
                raise ValueError('Transacao não encontrada.')
        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False
    
    def _generate_transacao_id(self):
        try:
            with open(self.TRANSACAO_JSON, 'r') as arquivo:
                transacoes = json.load(arquivo)
                if len(transacoes) == 0:
                    return 1
                else:
                    return transacoes[-1]['id'] + 1
        except json.decoder.JSONDecodeError:
            return 1
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False