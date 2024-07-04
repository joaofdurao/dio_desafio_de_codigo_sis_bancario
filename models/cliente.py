class Cliente:

    def __init__(self, id=None, nome=None, cpf=None, dt_nasc=None, endereco=None, senha=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.dt_nasc = dt_nasc
        self.endereco = endereco
        self.senha = senha

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.dt_nasc}\nEndereço: {self.endereco}"