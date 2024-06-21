#menu operações
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
                mensagem += "Sem saldo disponível\n"
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

#menu usuario
def verificar_usuario(menu, usuarios, cadastro):
    novo_usuario = {}
    opcao = int(input(menu))
    login = False
    usuario_logado = ""
    if opcao == 0:
        cadastro = False
        mensagem = "Volte Sempre!!!"
        login = False
    elif opcao == 1:
        novo_usuario, mensagem = cadastrar_usuario(usuarios=usuarios)
        login = False
    elif opcao == 2:
        cpf = str(input("Informe seu usuario (CPF): "))
        if validar_usuario(cpf=cpf, usuarios=usuarios):
            mensagem = f"\nSeja Bem vindo {buscar_nome_usuario(cpf=cpf, usuarios=usuarios)}!!"
            cadastro = False
            login = True
            usuario_logado = cpf
        else:
            mensagem = f"\nUsuário {cpf} não cadastrado!!"
    else:
        mensagem = "\nOperação inválida. Por favor selecione novamente a operação desejada."
    return novo_usuario, mensagem, cadastro, login, usuario_logado
            
def cadastrar_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    novo_usuario = {}

    if validar_usuario(cpf=cpf, usuarios=usuarios):
        mensagem = f"\nUsuário {cpf} já Cadastrado."
        return novo_usuario, mensagem
    else:
        nome = input("Informe o nome: ")
        dta_nasc = input("Informea a Data de Nascimento (formato DD/MM/YYYY): ")
        logradouro = input("Informe sua rua (sem nro): ")
        nro_endereco = input("Informe o número de sua casa: ")
        bairro = input("Informe seu bairro: ")
        cidade = input("Informe sua cidade: ")
        estado = input("Informe a sigla do seu estado: ")
        endereco = f"{logradouro} - {nro_endereco} - {bairro} - {cidade}/{estado}"
        novo_usuario = {cpf:{"nome":nome,"dta_nasc":dta_nasc,"endereco":endereco}}
        mensagem = f"\nUsuário {cpf} cadastrado com sucesso"
        return novo_usuario, mensagem

def validar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf in usuario:
            return True
        else:
            return False

def buscar_nome_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf in usuario:
            nome_usuario = usuario[cpf]
            return nome_usuario['nome']

#menu conta
def verificar_conta(menu, contas, cadastro, usuario, nro_conta):
    nova_conta = {}
    opcao = int(input(menu))
    movimentacao = False
    if opcao == 0:
        cadastro = False
        mensagem = "Volte Sempre!!!"
        movimentacao = False
    elif opcao == 1:
        nova_conta, mensagem, nro_conta = cadastrar_conta(usuario=usuario, nro_conta=nro_conta)
        contas.update(nova_conta)
        movimentacao = False
    elif opcao == 2:
        conta = input("Informe sua conta: ")
        usuario_logado = str(usuario)
        if validar_conta(conta=conta, contas=contas, usuario_logado=usuario_logado):
            mensagem = f"\nConta: {conta} - Agência: 0001!!"
            cadastro = False
            movimentacao = True
        else:
            mensagem = f"\nConta {conta} não cadastrada para o usuario {usuario}!!"
    else:
        mensagem = "\nOperação inválida. Por favor selecione novamente a operação desejada."
    return nova_conta, mensagem, cadastro, movimentacao, nro_conta

def cadastrar_conta(usuario, nro_conta):
    nro_conta += 1
    nova_conta = {str(nro_conta):{"agencia":"0001", "usuario":usuario}}
    mensagem = f"\nConta: {nro_conta}, Agência: 0001 Cadastrada com Sucesso para o usuário {usuario} - {buscar_nome_usuario(cpf=usuario, usuarios=usuarios)}"
    return nova_conta, mensagem, nro_conta 

def validar_conta(conta, contas, usuario_logado):
    if conta in contas:
        if contas[conta]["usuario"] == usuario_logado:
            return True
        else:
            return False
    else:
        return False 
    
#_____________________________________________________________________________________________________________________________#
#menus
menu_usuario = """
O que deseja fazer?

[0] Sair
[1] Novo Usuário
[2] Informar Usuário

=> """

menu_conta = """
O que deseja fazer?

[0] Sair
[1] Nova Conta
[2] Informar Conta

=> """

menu_operacao = """
O que deseja fazer?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#__________________________________________________________________________________________________________________________________________
#variaveis e constantes
saldo = 0
limite = 500
extrato = ""
numero_saques = 1
ultima_conta = 0

usuarios = []
contas = {}

LIMITE_SAQUES = 3

cadastro_usuario = True
cadastro_contas = True
login = False
movimentacao = False

while True:
    while cadastro_usuario:
        novo_usuario, mensagem, cadastro_usuario, login, usuario_logado = verificar_usuario(menu=menu_usuario, usuarios=usuarios, cadastro=cadastro_usuario)
        usuarios.append(novo_usuario)
        print(mensagem)
    if login:
        while cadastro_contas:
            nova_conta, mensagem, cadastro_contas, movimentacao, ultima_conta = verificar_conta(menu=menu_conta, contas=contas, cadastro=cadastro_contas, usuario=usuario_logado, nro_conta=ultima_conta)
            contas.update(nova_conta)
            print(contas)
            print(mensagem)
        if movimentacao:
            operacao = input(menu_operacao)
            if operacao.lower() == "d":
                valor = float(input("Qual o valor a ser depositado? "))
                saldo, mensagem, extrato = depositar(valor, saldo, extrato)
                print(mensagem)
            elif operacao.lower() == "s":
                if verifica_limite_saques(numero_saques):
                    valor = float(input("Qual o valor a ser sacado? "))
                    valor, saldo, extrato, limite, numero_saques,mensagem = sacar(valor=valor, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
                    print(mensagem)
                else:
                    print("Limite de Saques atingido.")
            elif operacao.lower() == "e":
                extrato = ver_extrato(saldo,extrato=extrato)
                print(extrato)
            elif operacao.lower() == "q":
                break
            else:
                print("Operação inválida. Por favor selecione novamente a operação desejada.")
        else:
            break
    else:
        break