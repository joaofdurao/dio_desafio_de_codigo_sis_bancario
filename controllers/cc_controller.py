from calendar import c
from models.conta_corrente import ContaCorrente
from repositories.cc_repository import CcRepository as CCRepo

class CCController:

    def criar_cc(self, cliente_id):
        cc = ContaCorrente(cliente_id = cliente_id)
        
        try: 
            CCRepo.create_cc(cc)
            return True  
        except Exception:
            return False

    def encontrar_cc_by_id(self, cc_id):
        try:
            cc = CCRepo.find_cc_by_id(cc_id)
            cc_dict = cc.__dict__
            return cc_dict
        except Exception:
            return False

    def listar_ccs(self):
        try:
            ccs = CCRepo.list_ccs()
            ccs_dict = []
            for i in ccs:
                ccs_dict.append(i.__dict__)
            return ccs_dict
        except Exception:
            return False

    def atualizar_cc(self, id_cc, saldo_cc = None, lmt_q_saque_cc = None, lmt_v_saque_cc = None):
        if lmt_q_saque_cc is not None or lmt_v_saque_cc is not None:
            if saldo_cc is None:
                try:
                    cc = ContaCorrente(id = id_cc, limite_qnt_saque = lmt_q_saque_cc, limite_vlr_saque = lmt_v_saque_cc)
                    CCRepo.update_cc(cc)
                    return True
                except Exception:
                    return False
            else:
                try:
                    cc = ContaCorrente(id = id_cc, saldo = saldo_cc, limite_qnt_saque = lmt_q_saque_cc, limite_vlr_saque = lmt_v_saque_cc)
                    CCRepo.update_cc(cc)
                    return True
                except Exception:
                    return False
        else:
            try:
                cc = ContaCorrente(id = id_cc, saldo = saldo_cc)
                CCRepo.update_cc(cc)
                return True
            except Exception:
                return False

    def deletar_cc(self, id_cc):
        try:
            CCRepo.delete_cc(id_cc)
            return True
        except Exception:
            return False    
        
    def depositar_valor(self, cc_id, deposito):
        if deposito >= 0:
            try:
                cc = self.encontrar_cc_by_id(cc_id)
                self.atualizar_cc(cc_id, saldo_cc = cc['saldo'] + deposito)
                return True
            except Exception:
                return False
        else:
            raise ValueError('Valor de depósito inválido.')
    
    def sacar_valor(self, cc_id, saque):
        if saque >= 0:
            try:
                cc = self.encontrar_cc_by_id(cc_id)
                if saque > cc['saldo'] and saque >= cc['limite_vlr_saque']:
                    self.atualizar_cc(cc_id, saldo_cc = cc['saldo'] - saque)
                    return True
                else:
                    raise ValueError('Saldo insuficiente ou valor de saque acima do limite.')
            except Exception:
                return False
        else:
            raise ValueError('Valor de saque inválido.')