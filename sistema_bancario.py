historico_bancario = []
historico_depositos = []
historico_saques = []
limite_saque = 0
saldo = 0.0

def atualizar_saldo(deposita, valor):
    """"Função para atualizar saldo bancário."""
    
    global saldo
    
    if deposita is True:
        saldo += valor
    else:
        saldo -= valor
    
def depositar_valor(valor_depositar):
    """"Função para depositar algum valor."""
    
    if valor_depositar <= 0:
        print("\n!! VALOR DE DEPOSITO NÃO ACEITO. !!\n")
        
    else:
        historico_bancario.append("D: R$" + str(valor_depositar))
        historico_depositos.append(valor_depositar)
        atualizar_saldo(True, valor_depositar)
        print(f"\n!! DEPOSITO DE R$ {valor_depositar} REALIZADO COM SUCESSO. !!\n")
        
def sacar_valor(valor_sacar):
    """"Função para sacar algum valor."""
    global limite_saque
    
    if valor_sacar == 0.0:
        print("\n!! SAQUE NEGADO. VALOR DE SAQUE INSUFICIENTE. !!\n")
        
    elif valor_sacar > 500.00:
        print ("\n!! SAQUE NEGADO. LIMITE DE R$ 500,00 ATINGIDO. !!\n") 
        
    elif valor_sacar > saldo:
        print ("\n!! SAQUE NEGADO. SALDO INSUFICIENTE. !!\n")
    
    else:
        historico_bancario.append("S: R$" + str(valor_sacar))
        historico_saques.append(valor_sacar)
        atualizar_saldo(False, valor_sacar)
        print(f"\n!! SAQUE DE R$ {valor_sacar} REALIZADO COM SUCESSO. !!\n")
        limite_saque += 1

def imprimir_extrato():  
    """"Função para imprimir extrato bancário.""" 
    
    if len(historico_bancario) == 0:
        print("\n!! AINDA NÃO FORAM REALIZADAS MOVIMENTAÇÕES. !!\n")
    
    else:
        print("--------------------".center(79))
        print("| Extrato bancário |".center(79))
        print("--------------------".center(79))
        
        for i in historico_bancario:
            print("".ljust(30) + "| " + i)    
     
        print(''.ljust(30) + '| SALDO TOTAL: R$'+ str(saldo) + "\n")

def inicio_view():
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

def back_menu():
    """Função lógica para funcionamento do menu principal."""
    
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
    
    inicio_view()
    while True:
        menu_view()
        option = back_menu()
        if option == 4:
            break



inicializar()
   