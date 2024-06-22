from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
    
    @property
    @abstractmethod
    def valor(self):
        pass

class Contaiterador:
    def __init__(self, contas):
        self.contas = contas
        self.contador = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self.contador]
            return f"""
                Agência:\t{conta.agencia}
                C/C:\t{conta.nro_conta}
                Titular:\t{conta.cliente.nome}
                Saldo:\t\tR$ {conta.saldo:.2f}
            """
        except IndexError:
            raise StopIteration
        finally:
            self.contador += 1

class Conta:
    def __init__(self, nro_conta, cliente):
        self._saldo = 0
        self._nro_conta = nro_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    @property
    def nro_conta(self):
        return self._nro_conta
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, nro_conta):
        nro_conta = nro_conta + 1
        return cls(nro_conta,cliente)
    
    def sacar(self, valor):
        saldo = self.saldo  #retorna valor da property saldo
        valor_valido = valor >= 0
        saldo_disponivel = valor <= saldo
        
        if valor_valido:
            if saldo_disponivel:
                self._saldo -= valor
                print("Saque liberado. Retire o dinheiro.")
                return True
            else:
                print("Sem saldo disponível\n")
        else:
            print("Valor Inválido. Por favor informe um valor válido!!")
        
        return False
        
    def depositar(self, valor):
        valor_valido = valor >= 0
        
        if valor_valido:
            self._saldo += valor
            print("Depósito realizado com sucesso.")
            return True
        else:
            print("Valor Inválido. Por favor informe um valor válido!!")
        
        return False

class ContaCorrente(Conta):
    def __init__(self, nro_conta, cliente, limite=500, limite_saques=3):
        super().__init__(nro_conta, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self._limite
        excedeu_saque = numero_saques >= self._limite_saques
        
        if excedeu_limite:
            print("\nSaque não liberado.\nValor acima do Limite disponível.")
        elif excedeu_saque:
            print("\nSaque não liberado.\nLimite de Saques atingido.")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t{self.nro_conta}
            Titular:\t{self.cliente.nome}
        """
        
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor    
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
        
    def gerar_relatorio(self, tipo_transacao):
        for transacao in self._transacoes:
            if tipo_transacao:
                if transacao['tipo'] == tipo_transacao:
                    yield transacao
            else:
                yield transacao
                
def log_transacao(func):
    def envelope(*args, **kwargs):
        reg_transacao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        resultado = func(*args, **kwargs)
        print(reg_transacao)
        return resultado
        
    return envelope     

def menu():
    menu = """\n
    O que deseja fazer?

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tNova Conta
    [l]\tListar Contas
    [u]\tNovo Cliente
    [q]\tSair

    => """
    
    return input(textwrap.dedent(menu))

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do Cliente: ")
    cliente = validar_cliente(cpf=cpf, clientes=clientes)
    
    if not cliente:
        print(f"\nUsuário {cpf} não cadastrado!!")
        return
    
    valor = float(input("Qual o valor a ser depositado? "))
    
    transacao = Deposito(valor=valor)
    
    conta = validar_conta(cliente=cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do Cliente: ")
    cliente = validar_cliente(cpf=cpf, clientes=clientes)
    
    if not cliente:
        print(f"\nUsuário {cpf} não cadastrado!!")
        return
    
    valor = float(input("Qual o valor do saque? "))
    
    transacao = Saque(valor=valor)
    
    conta = validar_conta(cliente=cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def ver_extrato(clientes):
    cpf = input("Informe o CPF do Cliente: ")
    cliente = validar_cliente(cpf=cpf, clientes=clientes)
    
    if not cliente:
        print(f"\nUsuário {cpf} não cadastrado!!")
        return
       
    conta = validar_conta(cliente=cliente)
    if not conta:
        return
    
    extrato_mov = ""
    tem_movimentacao = False

    menu_operacoes = """
        Qual operaçào deseja visualizar?
        
        [0]\tTodas
        [1]\tDepositos
        [2]\tSaques
        
        ==> """
    opcao = int(input(menu_operacoes))
    if opcao == 0:
        tipo_transacao = None
    elif opcao == 1:
        tipo_transacao = "Deposito"
    elif opcao == 2:
        tipo_transacao = "Saque"
    else:
        print("Opção inválida.")
        return
    for historico in conta.historico.gerar_relatorio(tipo_transacao=tipo_transacao):
        tem_movimentacao = True
        extrato_mov += f"\n{historico['tipo']}\t" if historico['tipo'] == 'Saque' else f"\n{historico['tipo']}\t"
        extrato_mov += f"\t-R$ {historico['valor']:.2f}" if historico['tipo'] == 'Saque' else f" R$ {historico['valor']:.2f}"
    if not tem_movimentacao:
        extrato_mov = "\nNão houve movimentações."
      
    extrato_cab = "\n########### EXTRATO ###########"               
    extrato_rod = "\n_______________________________"
    extrato_rod += f"\nSaldo Atual:     R$ {conta.saldo:.2f}"
    extrato_rod += "\n###############################"
    extrato = extrato_cab + extrato_mov + extrato_rod
    print(extrato)

@log_transacao
def cadastrar_conta(clientes, nro_conta, contas):
    cpf = input("Informe o CPF do Cliente: ")
    cliente = validar_cliente(cpf=cpf, clientes=clientes)
    
    if not cliente:
        print(f"\nUsuário {cpf} não cadastrado!!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, nro_conta=nro_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    mensagem = f"\n\tConta: {conta} Cadastrada com Sucesso para o cliente {cliente.cpf} - {cliente.nome}"
    print(mensagem) 

@log_transacao
def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = validar_cliente(cpf=cpf, clientes=clientes)
    
    if cliente:
        print(f"\nCliente {cpf} já cadastrado!!")
        return

    nome = input("Informe o nome: ")
    dta_nasc = input("Informea a Data de Nascimento (formato DD/MM/YYYY): ")
    logradouro = input("Informe sua rua (sem nro): ")
    nro_endereco = input("Informe o número de sua casa: ")
    bairro = input("Informe seu bairro: ")
    cidade = input("Informe sua cidade: ")
    estado = input("Informe a sigla do seu estado: ")
    endereco = f"{logradouro} - {nro_endereco} - {bairro} - {cidade}/{estado}"
    
    cliente =  PessoaFisica(nome=nome, data_nascimento=dta_nasc, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    
    mensagem = f"\nCliente {cpf} cadastrado com sucesso"
    print(mensagem)

def listar_contas(contas):
    #ToDo: alterar este bloco de código :: chamar o iterador ContaIterador
    for conta in Contaiterador(contas=contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def validar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def validar_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui conta cadastrada")
        return
    
    #FIXME: não permite cliente escolher a conta
    return cliente.contas[0]
    
def main():
    clientes = []
    contas = []
    
    while True:
        operacao = menu()
        if operacao == "d":
            depositar(clientes=clientes)
        elif operacao == "s":
            sacar(clientes=clientes)
        elif operacao == "e":
            ver_extrato(clientes=clientes)
        elif operacao == "c":
            nro_conta = len(contas) + 1
            cadastrar_conta(nro_conta=nro_conta, clientes=clientes, contas=contas)
        elif operacao == "l":
            listar_contas(contas)
        elif operacao == "u":
            cadastrar_cliente(clientes=clientes)
        elif operacao == "q":
            break
        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")
            
main()