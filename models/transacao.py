class Transacao:

    def __init__(self, id=None, valor=None, data=None, tipo=None, conta=None, cliente=None):
        self.id = id
        self.valor = valor
        self.data = data
        self.tipo = tipo
        self.conta = conta
        self.cliente = cliente

    def __str__(self):
        return f'{self.id} - {self.valor} - {self.data} - {self.tipo} - {self.conta} - {self.cliente}'