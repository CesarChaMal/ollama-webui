import os
from peewee import SqliteDatabase

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'ollama.db')
DB = SqliteDatabase(DB_PATH)
