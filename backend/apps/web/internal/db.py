import os

# Get the directory of the current file (main.py)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the database file
DB_PATH = os.path.join(CURRENT_DIR, 'data', 'ollama.db')

# Connect to the SqliteDatabase
DB = SqliteDatabase(DB_PATH)


#from peewee import *

#DB = SqliteDatabase("/content/backend/data/ollama.db")
#DB.connect()
