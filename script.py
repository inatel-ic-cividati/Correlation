#   Dev: Amor
#
#   Requirements:
#   
#   pip install beautifulsoup4

import sqlite3
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs4
from datetime import datetime
import time

conn = sqlite3.connect('wow.db')
cursor = conn.cursor()


class data:

    date = ''
    time = ''
    Us = ''
    Eu = ''
    Ch = ''
    Kr = ''
    Tw = ''

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
    print('Table created sucessfully')

def insertDatabase(data):
    try:
        
        values = data.date, data.time, data.Us ,data.Eu, data.Ch, data.Kr, data.Tw
        cursor.execute("""
        INSERT INTO wowtoken (date, time, Us, Eu, Ch, Kr, Tw)
        VALUES """+str(values)+"""
        """)
        conn.commit()
        print (data.time +' - Data inserted')

    except Exception as e:
        print('Problem in inserDatabase()!')
        print('Exception: ', e)

def getToken(data):

    url = 'https://wowtokenprices.com/'
    page = urlopen(url)
    soup = bs4(page, 'html.parser')
   
    aBox = soup.find_all('p', attrs={'class': 'money-text'})
    
    data.date = datetime.now().strftime("%m/%d/%Y")
    data.time = datetime.now().strftime("%H:%M:%S")
    data.Us = aBox[0].text.strip() # North America
    data.Eu = aBox[1].text.strip() # Europe
    data.Ch = aBox[2].text.strip() # China
    data.Kr = aBox[3].text.strip() # Korean
    data.Tw = aBox[4].text.strip() # Taiwan
    
def showValues(data):

    print ("time:", data.time)
    print ("date:", data.date)
    print ("US:", data.Us)
    print ("Eu:", data.Eu)
    print ("Ch:", data.Ch)
    print ("Kr:", data.Kr)
    print ("Tw:", data.Tw)

def fancyValues(data):

    print ('|    Us   |    Eu   |    Ch   |    Kr   |    Tw   |')
    print ('|',data.Us,'|', data.Eu,'|', data.Ch,'|', data.Kr,'|', data.Tw,'|')

def main():

    while (True):
        try:
            getToken(data)
            insertDatabase(data)
            fancyValues(data)
            #sleep 20 minuts
            #time.sleep(1800)
            
        except Exception as e:
            print ('Problme in main()')
            print ('Exception: ',e)
            conn.close()
            break

main()
