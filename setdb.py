import sqlite3

db = 'DB FOLDER HERE'
conn = sqlite3.connect(db)
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

    cursor.execute("""
    CREATE TABLE currency(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        Usd TEXT NOT NULL,
        Eur TEXT NOT NULL,
        Cny TEXT NOT NULL,
        Krw TEXT NOT NULL,
        Brl TEXT NOT NULL
    );
    """)

    print('Wowtoken database created sucessfully!')

setDatabase()

conn.close()
