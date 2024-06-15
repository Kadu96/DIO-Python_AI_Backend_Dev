def depositar(valor, saldo, extrato, /):
    if valor <= 0:
        mensagem = "Valor inválido para depósito. Por favor informe um valor válido." 
    else:
        mensagem = "Depósito realizado com sucesso."
        saldo += valor
        extrato += f"\nDeposito:        R$ {valor:.2f}"
    return saldo, mensagem, extrato

def sacar(*,valor, saldo, extrato, limite, numero_saques):
    if valor <= 0:
        mensagem = "Valor inválido para saque. Por favor informe um valor válido."
    else:
        if verifica_saldo(valor, limite):
            saldo -= valor
            numero_saques += 1
            extrato += f"\nSaque:          -R$ {valor:.2f}"
            mensagem = "Saque liberado. Retire o dinheiro."
        else:
            mensagem = "Saque não liberado.\n"
            if saldo < valor:
                mensagem += "Sem saldo disponível"
            if limite < valor:
                mensagem += "Valor acima do Limite disponível."
    return valor, saldo, extrato, limite, numero_saques, mensagem

def ver_extrato(saldo,/,*,extrato):
    extrato_cab = "\n########### EXTRATO ###########"
    extrato_mov = "\nNão houve movimentações." if not extrato else extrato
    extrato_rod = "\n_______________________________"
    extrato_rod += f"\nSaldo Atual:     R$ {saldo:.2f}"
    extrato_rod += "\n###############################"
    extrato = extrato_cab + extrato_mov + extrato_rod
    return extrato

def verifica_limite_saques(numero_saque):
    if numero_saque <= LIMITE_SAQUES:
        return True
    else:
        return False

def verifica_saldo(valor, limite):
    if valor <= saldo and valor <= limite:
        return True
    else:
        return False

def verifica_usuario(menu):
    while True:
        opcao = input(menu)
        if opcao == 0:
            break
        elif opcao == 1:
            cadastrar_usuario()
        else:
            verifica_operacao()

def verifica_operacao():
    menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
    while True:
        opcao = input(menu)
        if opcao.lower() == "d":
            valor = float(input("Qual o valor a ser depositado? "))
            saldo, mensagem, extrato = depositar(valor, saldo, extrato)
            print(mensagem)
        elif opcao.lower() == "s":
            if verifica_limite_saques(numero_saques):
                valor = float(input("Qual o valor a ser sacado? "))
                valor, saldo, extrato, limite, numero_saques,mensagem = sacar(valor=valor, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
                print(mensagem)
            else:
                print("Limite de Saques atingido.")
        elif opcao.lower() == "e":
            extrato = ver_extrato(saldo,extrato=extrato)
            print(extrato)
        elif opcao.lower() == "q":
            break
        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")
            
def cadastrar_usuario():
    usuario = {}
    return usuario["cpf"]

menu_user = """
[0] Sair
[1] Novo Usuário
[2] Ir para as Operações

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

verifica_usuario(menu_user)