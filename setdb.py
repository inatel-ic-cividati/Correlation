import sqlite3

def setDatabase(): 
    conn = sqlite3.connect('wow.db')
    cursor = conn.cursor()
    
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

    cursor.execute("""
    CREATE TABLE log(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        message TEXT
    );
    """)
    print ('Table log created sucessfully!')

    conn.close()

setDatabase()
