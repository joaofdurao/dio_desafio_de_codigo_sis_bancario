class ContaCorrente:
    _AGENCIA = '0001'
    _LIMITE_QNT_SAQUE = 3
    _LIMITE_VLR_SAQUE = 500.0

    def __init__(self, cliente, nr_conta, saldo):
        self.cliente = cliente
        self.agencia = self._AGENCIA
        self.nr_conta = nr_conta
        self.limite_qnt_saque = self._LIMITE_QNT_SAQUE
        self.limite_vlr_saque = self._LIMITE_VLR_SAQUE
        self.saldo = saldo
    