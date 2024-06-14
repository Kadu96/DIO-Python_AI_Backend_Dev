nome = "Carlos"
idade = 28
profissao = "Analista"
linguagem = "Python"

#interpolação com % :: raramente usada no python 3
print("\nOlá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.\n" % (nome,idade,profissao,linguagem))

#interpolação com Método Format :: permite reutilização da variavel dentro da string
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.\n".format(nome,idade,profissao,linguagem))

#interpolação com f-strings
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.\n")

valor = 10 / 3

print(f"O resultado é {valor}")
print(f"O resultado arredondado é {valor:.2f}\n")