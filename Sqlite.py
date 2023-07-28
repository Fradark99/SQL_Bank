import sqlite3
from pathlib import Path
from cadastroCliente import cadastrar
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.banco'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
conn = connection.cursor()
TABLE_NAME = 'CONTA'

# CRIA A TABELA
# cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}''(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, agencia TEXT, conta TEXT, saldo REAL, limite REAL)')

conn.execute(f"INSERT INTO {TABLE_NAME} (saldo) VALUES (0)")


conn.commit() #type: ignore






conn.close()
connection.close()