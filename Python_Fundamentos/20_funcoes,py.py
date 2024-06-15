def exibir_mensagem():
    print("Olá Mundo!")
    
def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
    
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor
    
exibir_mensagem()
exibir_mensagem2(nome="Carlos") # por nome e posição
exibir_mensagem2("Carlos") #por posição
exibir_mensagem2(**{"nome":"Carlos"}) # por nome e posição usando dict
exibir_mensagem3()
exibir_mensagem3("Carlos")
print()
print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))
print()

#def function (arg01, arg02, / , arg03, arg 04, *, arg05, arg06)
# arg01 e arg02 devem ser passado por posição obrigatoriamente
# arg03 e agr04 podem ser passado por posição ou por nome
# arg05 e arg06 devem ser passado por nome obrigatoriamente

def somar(a,b):
    return a + b

def exibir(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado de {a} + {b} é {resultado}")

op = somar

exibir(10, 10, somar)
print(op(15,25))