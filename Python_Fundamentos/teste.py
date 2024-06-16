contas = {"1":{"agencia":"0001", "usuario":"10"}, "2":{"agencia":"0001", "usuario":"5"}}
usuario = 10

def validar_conta(conta, contas, usuario_logado):
    for nro_contas in contas:
        if conta in nro_contas:
            if contas[conta]["usuario"] == usuario_logado:
                return True
            else:
                return False
        else:
            return False        

def validar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf in usuario:
            return True
        else:
            return False   
        
print(validar_conta(conta="1",contas=contas,usuario_logado=str(usuario))    )