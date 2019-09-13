import sqlite3

# creating the databse 
db_url = 'C:/YOUR/FOLDER/HERE/'
conn = sqlite3.connect(db_url+'wow.db')
cursor = conn.cursor()
print('wow.db created sucessfully!')

def setDatabase(): 
    try:
        # creating wowtoken table
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
        print('wowtoken table created sucessfully!')
    except sqlite3.Error as e:
            print("Database error: "+ e)

    try:
        # creating currency table
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

        print('currency table created sucessfully!')
    except sqlite3.Error as e:
            print("Database error: "+ e)

setDatabase()

conn.close()
