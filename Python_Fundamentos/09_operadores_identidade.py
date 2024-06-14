curso = "Curso de Python"
nome_curso = curso
saldo, limite = 500, 200

print(nome_curso is curso)
print(nome_curso is not curso)

print(curso is saldo)
print(saldo is limite)
print(saldo is not limite)