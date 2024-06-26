import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "db_dio_course.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row  # type: ignore


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )


def inserir_registro(conexao, cursor, nome, email):
    dados = (nome, email)
    try:
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu um erro! {e}")
        conexao.rollback


def atualizar_registro(conexao, cursor, nome, email, id):
    dados = (nome, email, id)
    try:
        cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", dados)
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu um erro! {e}")
        conexao.rollback


def excluir_registro(conexao, cursor, id):
    dados = (id,)
    try:
        cursor.execute("DELETE FROM clientes WHERE id=?;", dados)
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu um erro! {e}")
        conexao.rollback


def inserir_varios(conexao, cursor, dados):
    try:
        cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
        conexao.commit()
    except Exception as e:
        print(f"Ocorreu um erro! {e}")
        conexao.rollback


def recuperar_cliente(conexao, cursor, id):

    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_cliente(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome")


# inserir_registro(conexao=conexao, cursor=cursor, nome="Carlos", email="cadusilva@gmail.com")
# atualizar_registro(conexao=conexao, cursor=cursor, nome="Carlos Eduardo", email="cadusilva96@gmail.com", id=2)
# excluir_registro(conexao=conexao, cursor=cursor, id=3)

dados = [
    ("Guilherme", "guilherme@gmail.com"),
    ("Ana", "ana@gmail.com"),
    ("Gustavo", "gustavo@gmail.com"),
    ("Maria", "maria@gmail.com"),
]
# inserir_varios(conexao=conexao, cursor=cursor, dados=dados)

clientes = listar_cliente(cursor=cursor)
for cliente in clientes:
    print(dict(cliente))

# cliente = recuperar_cliente(conexao=conexao, cursor=cursor, id=2)
# print(dict(cliente))

# id_cliente = input("Informe o ID do cliente: ")
# cursor.execute("SELECT * FROM clientes WHERE id=?", id_cliente)
# clientes = cursor.fetchall()
# for cli in clientes:
#     print(dict(cli))

# try:
#     cursor.execute("INSERT INTO clientes (nome, email) VALUES ('teste1','teste1@email.com');")
#     cursor.execute("INSERT INTO clientes (nome, email) VALUES (4,'teste2','teste2@email.com');")
#     conexao.commit()
# except Exception as e:
#     print(f"Ocorreu um erro! {e}")
#     conexao.rollback
