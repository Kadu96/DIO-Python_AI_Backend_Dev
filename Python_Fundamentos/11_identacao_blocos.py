def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print ("Valor Sacado!")
        saldo -= valor
        
    print(f"seu Saldo atual é {saldo}")
    
def depositar(valor):
    saldo = 500
    saldo += valor

depositar(250)        
sacar(1000)