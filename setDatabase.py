import sqlite3
import os
from data import database as db

def set_Table(tableName): 
    try:
        # creating wowtoken table
        colunmName = tableName.replace("wowtoken_","")
        colunmName = colunmName.replace("currency_","")

        cursor.execute("""
        CREATE TABLE """+tableName+"""(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            time INT NOT NULL,
            """+colunmName+""" FLOAT NOT NULL
        );
        """)
        print(tableName+' table created sucessfully!')

    except sqlite3.Error as e:
            print(tableName + " error: ", e)

# creating the databse 
conn = db.get_connection('wow.db')
cursor = conn.cursor()
print('wow.db created sucessfully!')

params = ['us', 'eu', 'china', 'korea', 'taiwan']

for table in params:
    set_Table('wowtoken_'+table)
    set_Table('currency_'+table)

conn.close()
