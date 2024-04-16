historico_bancario = []
historico_depositos = []
historico_saques = []
limite_saque = 0
saldo = 0.0

def atualizar_saldo(deposita, valor):
    global saldo
    
    if deposita == True:
        saldo += valor
    else:
        saldo -= valor
    

def depositar_valor(valor_depositar):
    if valor_depositar <= 0:
        print("Valor de deposito não aceito.")
    else:
        historico_bancario.append("D: R$" + str(valor_depositar))
        historico_depositos.append(valor_depositar)
        atualizar_saldo(True, valor_depositar)
        print(f"DEPOSITO DE R$ {valor_depositar} REALIZADO COM SUCESSO.")
        
def sacar_valor(valor_sacar):
    global limite_saque
    if limite_saque == 3:
        print("Saque negado. Limite diário atingido.")
        
    elif saldo == 0.0:
        print ("Saque negado. Saldo insuficiente.")
    
    else:
        if valor_sacar > saldo:
            print ("Saque negado. Saldo insuficiente.")
        
        elif valor_sacar > 500.00:
            print ("Saque negado. Limite de R$500.00 atingido")
            
        else: 
            historico_bancario.append("S: R$" + str(valor_sacar))
            historico_saques.append(valor_sacar)
            atualizar_saldo(False, valor_sacar)
            print(f"SAQUE DE R$ {valor_sacar} REALIZADO COM SUCESSO.")
            limite_saque += 1

def imprimir_extrato():
    if len(historico_bancario) == 0:
        print("Não foram realizadas movimentações.")
    
    else:
        print("----------------")
        print("Extrato bancário")
        print("----------------")
        
        for i in historico_bancario:
            print(i)    
     
        print(f'SALDO TOTAL: R$ {saldo}')

def inicio_view():
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
        print(line)

def back_menu():
    option = int(input("Escolha uma das opcoes acima: "))

    if option == 1:
        deposito_view()
        return option
        
    elif option == 2:
        saque_view()
        return option
    
    elif option == 3:
        imprimir_extrato()
        return option
    
    elif option == 4:
        return option
    
    else:
        print("Opção invalida.")
        
def deposito_view():
    valor_deposito = float(input("Indique o valor a ser depositado: "))
    depositar_valor(valor_deposito)
    
    
def saque_view():
    valor_saque = float(input("Indique o valor a ser sacado: "))
    sacar_valor(valor_saque)
    
        
def inicializar():
    option = 0
    
    inicio_view()
    while True:
        menu_view()
        option = back_menu()
        if option == 4:
            break



inicializar()
   