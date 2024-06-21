menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.lower() == "d":
        
        valor = float(input("Qual o valor a ser depositado? "))
        if valor <= 0:
            print("Valor inválido para depósito. Por favor informe um valor válido.") 
        else:
            saldo += valor
            extrato += f"\nDeposito:        R$ {valor:.2f}"
        
    elif opcao.lower() == "s":
        
        valor = float(input("Qual o valor a ser sacado? "))
        if valor <= 0:
            print("Valor inválido para saque. Por favor informe um valor válido.")
        else:
            if numero_saques <= LIMITE_SAQUES:
                if valor <= saldo and valor <= limite:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"\nSaque:          -R$ {valor:.2f}"
                    print("Saque liberado. Retire o dinheiro.")
                else:
                    print("Saque não liberado.\n")
                    if saldo < valor:
                        print("Sem saldo disponível")
                    if limite < valor:
                        print("Valor acima do Limite disponível.")
            else:
                print("Limite de Saques atingido.")
                
    elif opcao.lower() == "e":
        print("\n########### EXTRATO ###########")
        print("\nNão houve movimentações." if not extrato else extrato)
        print("\n_______________________________")
        print(f"\nSaldo Atual:     R$ {saldo:.2f}")
        print("\n###############################")
        
    elif opcao.lower() == "q":
        break
    else:
        print("Operação inválida. Por favor selecione novamente a operação desejada.")