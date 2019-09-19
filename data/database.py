import sqlite3
import os

# Get root project path i.g: C:/Users/Documents/Project
dir_path = os.path.dirname(__file__)
# Create database in C:/Users/Documents/Project/wow.db
db_url = dir_path + '/'

def get_db_path():
    return dir_path

def get_connection(db_name):
    return sqlite3.connect(db_url + db_name)
