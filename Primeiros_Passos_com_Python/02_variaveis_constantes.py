idade = 28
nome = 'Carlos Eduardo da Silva'

#Constantes devem ser declaradas em letras maiusculas
ABS_PATH = """C:/Users/admel/Documents/Github/DIO-Python_AI_Backend_Dev"""
DEBUG = True
BRAZILIAN_STATES = ['SP', 'PR', 'SC']
AMOUNT = 30.5

print(f'\nMeu nome é {nome} e tenho {idade} anos.')

idade, nome = (29, "Eduardo") #parenteses são opcionais :: idade, nome = 29, "Eduardo" tbm funcionará
print(f'Meu nome é {nome} e tenho {idade} anos.')

print(f'\nEste arquivo está no caminho {ABS_PATH}.')

limite_saque_diario = 1000 #sempre usar nomes sugestivos, evitar abreviações

