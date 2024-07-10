from math import e
from re import T
import re
from models.transacao import Transacao
from repositories.transacao_repository import TransacaoRepository as TRepo


class TransacaoController:
    def criar_transacao(self, valor, data, tipo, conta, cliente):
        transacao = Transacao(valor=valor, data=data, tipo=tipo, conta=conta, cliente=cliente)
        try:
            TRepo.create_transacao(transacao)
            return True
        except Exception:
            return False

    def encontrar_transacao(self, id_transacao):
        try:
            transacao = TRepo.find_transacao_by_id(id_transacao)
            transacao_dict = transacao.__dict__
            return transacao_dict
        except Exception:
            return False

    def listar_transacoes(self):
        try:
            transacoes = TRepo.list_transacoes
            transacoes_dict = []
            for i in transacoes:
                transacoes_dict.append(i.__dict__)
            return transacoes_dict
        except Exception:
            return False

    def atualizar_transacao(self, id_transacao, valor=None, data=None, tipo=None, conta=None, cliente=None):
        try:
            transacao = Transacao(id=id_transacao, valor=valor, data=data, tipo=tipo, conta=conta, cliente=cliente)
            TRepo.update_transacao(transacao)
            return True
        except Exception:
            return False

    def deletar_transacao(self, id_transacao):
        try:
            TRepo.delete_transacao(id_transacao)
            return True
        except Exception:
            return False
        
    def listar_transacoes_por_cliente(self, id_cliente):
        try:
            transacoes = TRepo.list_transacoes()
            transacoes_dict = []
            for i in transacoes:
                if i.cliente['id'] == id_cliente:
                    transacoes_dict.append(i.__dict__)
            return transacoes_dict
        except Exception:
            return False
        
    def listar_transacoes_por_conta(self, id_conta):
        try:
            transacoes = TRepo.list_transacoes()
            transacoes_dict = []
            for i in transacoes:
                if i.conta['id'] == id_conta:
                    transacoes_dict.append(i.__dict__)
            return transacoes_dict
        except Exception:
            return False 