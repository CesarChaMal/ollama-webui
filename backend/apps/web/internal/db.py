import os
from peewee import *

# Get the absolute path of the directory where this script is located
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Assuming the base directory is two levels up from the current directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR)))

# Construct the path to the database file
# This makes the path relative to the /content directory
DB_PATH = os.path.join(BASE_DIR, 'data', 'ollama.db')

print("Current Directory:", CURRENT_DIR)
print("Base Directory:", BASE_DIR)
print("Database Path:", DB_PATH)
print("Database Exists:", os.path.exists(DB_PATH))

DB = SqliteDatabase(DB_PATH)


#from peewee import *

#DB = SqliteDatabase("/content/backend/data/ollama.db")
#DB.connect()
