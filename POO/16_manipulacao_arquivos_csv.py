import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
COL_ID = 0
COL_NOME = 1

try:
    with open(ROOT_PATH/"arquivos_teste"/"usuarios.csv", "w", newline="", 
              encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'carlos'])
        escritor.writerow(['2', 'eduardo'])
except IOError as exc:
    print(f"Erro na abertura do arqivo!\n{exc}")
    
try:
    with open(ROOT_PATH/"arquivos_teste"/"usuarios.csv", "r", newline="", 
              encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[COL_ID], row[COL_NOME])
except IOError as exc:
    print(f"Erro na abertura do arqivo!\n{exc}")    
print()
    
try:
    with open(ROOT_PATH/"arquivos_teste"/"usuarios.csv", "r", newline="", 
              encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro na abertura do arqivo!\n{exc}")
