import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Leitura de Arquivo

arquivo = open(ROOT_PATH/"arquivos_teste"/"lorem.txt", "r")

# print(arquivo.read())       #tofo o conteudo
print(arquivo.readline())   #apenas a linha
# print(arquivo.readlines())  #todo o conteudo em formato de lista

# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()

# Escrever Arquivo

arquivo = open(ROOT_PATH / "arquivo_teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\nEscrevendo ", "um ", "novo ", "texto"])

arquivo.close

# Gerenciando arquivos e diretorios

#os.mkdir(ROOT_PATH / "arquivos_teste") #cria novo diretorio
shutil.move(ROOT_PATH/"arquivo_teste.txt", ROOT_PATH/"arquivos_teste"/"arquivo_teste.txt")  #altera o dir de um arquivo

os.rename(ROOT_PATH/"arquivos_teste"/"arquivo_teste.txt", ROOT_PATH/"arquivos_teste"/"arquivo_novo_01.txt") #renomeia um arquivo

#os.remove(ROOT_PATH/"arquivos_teste/arquivo_novo_01.txt")   #apaga um arquivo

#Tratando exceções / erros

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print(f"Arquivo não encontrado!!\n{exc}")
except IsADirectoryError as exc:
    print(f"Não foi possivel abrir o arquivo!!\n{exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo!!\n{exc}")
except Exception as exc:
    print(f"Algum erro ocorreru na abertura do arquivo!!\n{exc}") 
   
print()    
#Boas Praticas

try:
    with open(ROOT_PATH/"arquivos_teste"/"novo_exemplo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ação de manipulação de arquivos em Python")
except IOError as exc:
    print(f"Erro ao abrir o arquivo!!\n{exc}") 
    
try:
    with open(ROOT_PATH/"arquivos_teste"/"novo_exemplo.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo!!\n{exc}")       
except UnicodeDecodeError as exc: 
    print(f"Erro de codificação!!\n{exc}")          