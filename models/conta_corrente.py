class ContaCorrente:
    _AGENCIA = '0001'
    _LIMITE_QNT_SAQUE = 3
    _LIMITE_VLR_SAQUE = 500.0

    def __init__(self, id=None, agencia = _AGENCIA,  nr_conta=None, cliente=None, saldo=0.0, limite_qnt_saque = _LIMITE_QNT_SAQUE, limite_vlr_saque = _LIMITE_VLR_SAQUE):
        self.id = id
        self.agencia = agencia
        self.nr_conta = nr_conta
        self.cliente = cliente
        self.saldo = saldo
        self.limite_qnt_saque = limite_qnt_saque
        self.limite_vlr_saque = limite_vlr_saque
    
    def __str__(self):
        return f'Id: {self.id}, Agencia: {self.agencia}, Conta: {self.nr_conta}, Cliente: {self.cliente}, Saldo: {self.saldo}'