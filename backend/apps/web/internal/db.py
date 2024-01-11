import os
from peewee import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(CURRENT_DIR, 'data', 'ollama.db')

print("Current Directory:", CURRENT_DIR)
print("Database Path:", DB_PATH)
print("Database Exists:", os.path.exists(DB_PATH))

DB = SqliteDatabase(DB_PATH)


#from peewee import *

#DB = SqliteDatabase("/content/backend/data/ollama.db")
#DB.connect()
