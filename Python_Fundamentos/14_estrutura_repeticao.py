texto =  "exemplo"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
print()

for numero in range(11):
    print(numero, end="")

print()

for numero in range(0, 51, 5):
    print(numero, end="")
    
opcao = -1

print()

while opcao != 0:
    opcao = int(input("\n[1] Sacar \n[2] Extrato \n[0] Sair\n"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Mostrando o Extrato")
    elif opcao == 0:
        break
    else:
        print("Opção inválida!!\n")
print("Obrigado e volte sempre!\n")

while True:
    for numero in range(0, 51, 5):
        if numero % 2 == 0:
            continue
        print(numero, end=",")
    break

print()