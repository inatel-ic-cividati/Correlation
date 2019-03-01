#   Dev: Amor

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
    message = ''
    Us = ''
    Eu = ''
    Ch = ''
    Kr = ''
    Tw = ''

def insertData(data):

    try:  
        values = data.date, data.time, data.Us ,data.Eu, data.Ch, data.Kr, data.Tw
        cursor.execute("""
        INSERT INTO wowtoken (date, time, Us, Eu, Ch, Kr, Tw)
        VALUES """+str(values)+"""
        """)
        conn.commit()
        print ('Data inserted at '+data.time)
        data.message = ''

    except Exception as e:
        data.message = str(e)
        print ('Problem in insertData()!')
        print ('Exception: ', e)
        values = data.date, data.time, data.message
        cursor.execute("""
        INSERT INTO log (date, time, message)
        VALUES """+str(values)+"""
        """)
        conn.commit()

def getToken(data):

    data.date = datetime.now().strftime("%m/%d/%Y")
    data.time = datetime.now().strftime("%H:%M:%S")
    try:
        url = 'https://wowtokenprices.com/'
        page = urlopen(url)
        soup = bs4(page, 'html.parser')
    
        aBox = soup.find_all('p', attrs={'class': 'money-text'})
        
        data.Us = aBox[0].text.strip() # North America
        data.Eu = aBox[1].text.strip() # Europe
        data.Ch = aBox[2].text.strip() # China
        data.Kr = aBox[3].text.strip() # Korean
        data.Tw = aBox[4].text.strip() # Taiwan

    except Exception as e:
        print ('Problem in getToken()!')
        print ('Exception: ',e)
        data.message = str(e)

def showValues(data):

    print ("time:", data.time)
    print ("date:", data.date)
    print ("message:", data.message)
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
            insertData(data)
            fancyValues(data)
            #sleep 20 minuts
            time.sleep(1200)
            
        except Exception as e:
            print ('Problem in main()')
            print ('Exception: ',e)
            conn.close()
            
main()
