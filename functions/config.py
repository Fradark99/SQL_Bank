import sys  
from time import sleep
import os   
import sqlite3
from pathlib import Path
from abc import ABC, abstractmethod

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.banco'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
conn = connection.cursor()
conn = sqlite3.connect('db.banco')
cursor = conn.cursor() # type: ignore
TABLE_NAME = 'CONTA'

conn.execute(f"INSERT INTO {TABLE_NAME} (saldo) VALUES (0)")









