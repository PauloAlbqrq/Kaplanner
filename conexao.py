import sqlite3

arquivo_db = "planner.db"


def conectar_db():
    conexao = None
    try:
        conexao = sqlite3.connect(arquivo_db)
    except sqlite3.Error as error:
        print(f"Erro ao conectar ao banco de dados:\n{error}")
    return conexao

def desconectar_db(conexao):
    if conexao:
        conexao.close()
    