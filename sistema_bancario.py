import logging
from operator import index


lista_clientes = []
cliente_ativo = None
lista_contas = []
conta_ativa = None
# ------------------------------->> Modelos

# Entidade Conta Corrente
AGENCIA = '0001'
nr_conta = 0
historico_bancario = []
historico_depositos = []
historico_saques = []
limite_saque = 0
saldo = 0.0

# Entidade Cliente
ENDERECO_CLIENTE = f'{logradouro},{nr},{bairro},{cidade}/{sigla_estado}'
nome_cliente = ''
dt_nasc_cliente = ''
cpf_cliente = ''
contas_cliente = []

cliente = {
    'nome': nome_cliente, 
    'dt_nasc': dt_nasc_cliente,
    'cpf': cpf_cliente,
    'endereço': ENDERECO_CLIENTE,
    'contas': []

}

conta_corrente = {
    'cliente': cliente['cpf'],
    'agencia': AGENCIA,
    'nr_conta': nr_conta,
    'hist_bancario': [],
    'hist_depositos': [],
    'hist_saques': [],
    'limite_saque': 0,
    'saldo': 0.0
}

def atualizar_saldo(conta, deposita, valor):
    """"Função para atualizar saldo bancário."""

    conta['saldo'] += valor if deposita else -valor
    
def depositar_valor(valor_depositar, conta):
    """"Função para depositar algum valor."""
    
    if valor_depositar <= 0:
        print("\n!! VALOR DE DEPOSITO NÃO ACEITO. !!\n")
        
    else:
        conta['hist_bancario'].append("D: R$" + str(valor_depositar))
        conta['hist_depositos'].append(valor_depositar)
        atualizar_saldo(conta, True, valor_depositar)
        print(f"\n!! DEPOSITO DE R$ {valor_depositar} REALIZADO COM SUCESSO. !!\n")
        
def sacar_valor(valor_sacar, conta):
    """"Função para sacar algum valor."""
    
    if valor_sacar == 0.0:
        print("\n!! SAQUE NEGADO. VALOR DE SAQUE INSUFICIENTE. !!\n")
        
    elif valor_sacar > 500.00:
        print ("\n!! SAQUE NEGADO. LIMITE DE R$ 500,00 ATINGIDO. !!\n") 
        
    elif valor_sacar > conta['saldo']:
        print ("\n!! SAQUE NEGADO. SALDO INSUFICIENTE. !!\n")
    
    else:
        conta['hist_bancario'].append("S: R$" + str(valor_sacar))
        conta['hist_saques'].append(valor_sacar)
        atualizar_saldo(conta, False, valor_sacar)
        print(f"\n!! SAQUE DE R$ {valor_sacar} REALIZADO COM SUCESSO. !!\n")
        conta['limite_saque'] += 1

def cadastrar_cliente():

def validar_cliente(cpf):
    global cliente_ativo
    try: 
        cliente_ativo = lista_clientes[index(lista_clientes.cliente['cpf'] == cpf)]
        return True
    except:
        return False

def cadastrar_conta(cliente):

def selecionar_conta(cliente):

def verificar_conta(cliente):
    if len(cliente['contas']):
        return True
    else:
        return False
# ------------------------------->> Controladores

def find_cliente_controller(cpf):
    if validar_cliente(cpf):
        return True
    else:
        return False

# ------------------------------->> Interfaces

def imprimir_extrato(conta):  
    """"Função para imprimir extrato bancário.""" 
    
    if len(conta['hist_bancario']) == 0:
        print("\n!! AINDA NÃO FORAM REALIZADAS MOVIMENTAÇÕES. !!\n")
    
    else:
        print("--------------------".center(79))
        print("| Extrato bancário |".center(79))
        print("--------------------".center(79))
        
        for i in conta['hist_bancario']:
            print("".ljust(30) + "| " + i)    
     
        print(''.ljust(30) + '| SALDO TOTAL: R$'+ str(conta['saldo']) + "\n")

def imprimir_banner():
    """Função de inícialização do programa."""
    
    banco_dio = [
        " ------------------------------------------------------------------------------",
        " #######   #######  ##     ## ######## ########     #######  ######## ######## ",
        " ##    ## ##     ## ###    ## ##       ##    ##     ##    ##    ##    ##    ## ",
        " ##    ## ##     ## ####   ## ##       ##    ##     ##     #    ##    ##    ## ",
        " #######  ######### ## ##  ## ##       ##    ## ### ##     #    ##    ##    ## ",
        " ##    ## ##     ## ##  ## ## ##       ##    ##     ##     #    ##    ##    ## ",
        " ##    ## ##     ## ##    ### ##       ##    ##     ##    ##    ##    ##    ## ",
        " #######  ##     ## ##     ## ######## ########     #######  ######## ######## ",
        " ------------------------------------------------------------------------------",
    ]

    for line in banco_dio:
        print(line)

def login_menu():
    """Função para a tela de login."""

    options = [
        "-----------------",
        "|   BANCO DIO   |",
        "-----------------",
        "| 1- LOGIN      |",
        "| 2- CADASTRAR  |",
        "-----------------"
    ]

    for line in options:
        print(line.center(79))

    option = int(input(">>> Escolha uma das opcoes acima: "))
    
    if option == 1:
        cpf = input(">>> Digite o CPF: ")
        if find_cliente_controller(cpf):
            logging.info("Login realizado com sucesso.")
            if find_conta_controller(cliente_ativo):
                selecionar_conta(cliente)    
                menu_view()
            else:
                cadastrar_conta(cliente_ativo)                
                menu_view()
        else:
            logging.error("Cliente não encontrado.")
            login_view()
    
    elif option == 2:
        cadastrar_cliente()
        login_view()
    
    else:
        print("\n!! OPÇÃO INVÁLIDA !!\n")
        login_view()

def menu_view():
    """Função para menu do programa."""
    
    menu_inicial = [
        "-----------------",
        "|   BANCO DIO   |",
        "-----------------",
        "| 1- DEPOSITAR  |",
        "| 2- SACAR      |",
        "| 3- EXTRATO    |",
        "| 4- SAIR       |",
        "-----------------"
    ]
    
    for line in menu_inicial:
        print(line.center(79))

        option = int(input(">>> Escolha uma das opcoes acima: "))

    if option == 1:
        deposito_view()
        return option
        
    elif option == 2:
        if limite_saque == 3:
            print("\n!! SAQUE NEGADO. LIMITE DIÁRIO ATINGIDO. !!\n")
            
        elif saldo == 0.0:
            print("\n!! SAQUE NEGADO. SALDO EM CONTA INSUFICIENTE. !!\n")
            
        else:
            saque_view()
            
        return option
    
    elif option == 3:
        imprimir_extrato()
        return option
    
    elif option == 4:
        return option
    
    else:
        print("\n!! OPÇÃO INVÁLIDA !!\n")
        return option


def deposito_view():
    """Função interativa para a operação de depósito."""
    
    valor_deposito = float(input(">>> Indique o valor a ser depositado: "))
    depositar_valor(valor_deposito)


def saque_view():
    """Função interativa para a operação de saque."""
    
    valor_saque = float(input(">>> Indique o valor a ser sacado: "))
    sacar_valor(valor_saque)
    
        

















def inicializar():
    """Função para rodar o sistema."""
    
    option = 0
    
    imprimir_banner()
    while True:
        menu_view()
        if option == 4:
            break
















inicializar()
   