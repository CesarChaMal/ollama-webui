import os
from peewee import *

# Get the directory of the current file (db.py)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up two levels from the current directory to reach the base directory
BASE_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))

# Construct the path to the database file
DB_PATH = os.path.join(BASE_DIR, 'data', 'ollama.db')

print("Base Directory:", BASE_DIR)
print("Database Path:", DB_PATH)
print("Database Exists:", os.path.exists(DB_PATH))

DB = SqliteDatabase(DB_PATH)


#from peewee import *

#DB = SqliteDatabase("/content/backend/data/ollama.db")
#DB.connect()
