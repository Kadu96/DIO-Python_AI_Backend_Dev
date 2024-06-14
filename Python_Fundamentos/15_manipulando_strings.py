curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso = "    Python  "

print(curso.strip() + ".")
print(curso.lstrip() + ".")
print(curso.rstrip() + ".")

curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))
print()

#fatiamento de string
nome = "Carlos Eduardo da Silva"

print(nome[0])
print(nome[:7])
print(nome[7:])
print(nome[7:14])
print(nome[7:14:2])
print(nome[:])
print(nome[::-1])
print()

#string múltiplas linhas
mensagem = f"""
    Olá meu nome é {nome}
Eu estou aprendendo Python.
      Essa mensagem tem diferente recuos.
"""
print(mensagem)