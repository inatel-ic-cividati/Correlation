import sqlite3

conn = sqlite3.connect('wow.db')
cursor = conn.cursor()

def setDatabase(): 
    
    cursor.execute("""
    CREATE TABLE wowtoken(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        Us TEXT NOT NULL,
        Eu TEXT NOT NULL,
        Ch TEXT NOT NULL,
        Kr TEXT NOT NULL,
        Tw TEXT NOT NULL
    );
    """)
    print('Table wowtoken created sucessfully!')

def updateDatabase ():
    
    cursor.execute("""
    CREATE TABLE currency(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        Usd TEXT NOT NULL,
        Eur TEXT NOT NULL,
        Cny TEXT NOT NULL,
        Krw TEXT NOT NULL
    );
    """)
    print('Table currency created sucessfully!')

setDatabase()

conn.close()
