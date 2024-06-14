MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Menor de idade, não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor de idade, não pode tirar a CNH")

'''
saldo = 2000

saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizado saque!")

if saldo < saque:
    print("Sem saldo suficiente!")

if saldo >= saque:
    print("Realizado saque!")
else:
    print("Sem saldo suficiente!")
'''