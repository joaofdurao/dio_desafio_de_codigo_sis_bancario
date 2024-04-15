historico_bancario = []
historico_depositos = []
historico_saques = []
limite_saque = 0
saldo = 0.0

def atualizar_saldo():
    saldo = sum(historico_depositos) - sum(historico_saques)
    

def depositar_valor(valor_depositar):
    if valor_depositar <= 0:
        print("Valor de deposito não aceito.")
    else:
        historico_bancario.append("D: R$ " + valor_depositar)
        historico_depositos.append(valor_depositar)
        atualizar_saldo()
        print(f"DEPOSITO DE R$ {valor_depositar} REALIZADO COM SUCESSO.")
        
def sacar_valor(valor_sacar):
    if limite_saque == 3:
        print("Saque negado. Limite diário atingido.")
        
    elif saldo == 0.0:
        print ("Saque negado. Saldo insuficiente.")
    
    else:
        if valor_sacar > saldo:
            print ("Saque negado. Saldo insuficiente.")
        
        elif valor_sacar > 500.00:
            print ("Saque negado. Limite de R$ 500.00 atingido")
            
        else: 
            historico_bancario.append("S: R$ " + valor_sacar)
            historico_saques.append(valor_sacar)
            atualizar_saldo()
            print(f"DEPOSITO DE R$ {valor_sacar} REALIZADO COM SUCESSO.")

def imprimir_extrato():
    if len(historico_bancario) == 0:
        print("Não foram realizadas movimentações.")
    
    else:
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










inicio_view()
   