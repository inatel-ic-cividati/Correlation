#   Dev: Amor

import sqlite3
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs4
from datetime import datetime
import time as t
import json
import requests


dbdirectory = 'db directory here.db'
conn = sqlite3.connect(dbdirectory)
cursor = conn.cursor()

date = datetime.now().strftime("%m/%d/%Y")
time = ''

dateDict = {

    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Set": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
}

class Token:
    
    Date = datetime.now().strftime("%m/%d/%Y")
    Time = datetime.now().strftime("%H:%M:%S")
    Us = ''
    Eu = ''
    Ch = ''
    Kr = ''
    Tw = ''

class Currency:

    Date = ''
    Time = ''
    Usd = ''
    Eur = ''
    Cny = ''
    Krw = ''
    Brl = ''


def insertData(Token, Currency):

    try:  

        #   insert Token
        values = Token.Date, Token.Time, Token.Us ,Token.Eu, Token.Ch, Token.Kr, Token.Tw
        cursor.execute("""
        INSERT INTO wowtoken (date, time, Us, Eu, Ch, Kr, Tw)
        VALUES """+str(values)+"""
        """)
        conn.commit()

        #   insert Currency 
        values = Currency.Date, Currency.Time, Currency.Usd, Currency.Eur, Currency.Cny, Currency.Krw, Currency.Brl
        cursor.execute("""
        INSERT INTO currency (date, time, Usd, Eur, Cny, Krw, Brl)
        VALUES """+str(values)+"""
        """)
        conn.commit()

        print (Token.Date+' - '+Token.Time+' Data inserted.')

        return True

    except Exception as e:
        print (Token.date+' - '+Token.time+' Problem in insertData().')
        print ('Exception: ', e)

        return False

def setCurrency(Currency):
    
    try:
        r = requests.get('https://api.exchangeratesapi.io/latest?symbols=USD,BRL,EUR,CNY,KRW&base=USD')
        
        dateModel = (r.headers['Date'])[5:16]
        dateSplitted = dateModel.split()
        dateModel = dateDict[dateSplitted[1]] + "/" + dateSplitted[0] + "/" + dateSplitted[2]
        timeModel = (r.headers['Date'])[17:25]
        
        js = r.json()

        Currency.Usd = '1'
        Currency.Eur = js["rates"]["EUR"]
        Currency.Cny = js["rates"]["CNY"]
        Currency.Krw = js["rates"]["KRW"]
        Currency.Brl =  js["rates"]["BRL"]
        Currency.Time = timeModel
        Currency.Date = dateModel

        return True

    except Exception as e:
        print (Token.Date+' - '+Token.Time+' Problem in setCurrency()!')
        print ('Exception: ',e)

        return e

def setToken(Token):

    Token.Date = datetime.now().strftime("%m/%d/%Y")
    Token.Time = datetime.now().strftime("%H:%M:%S")

    try:
        url = 'https://wowtokenprices.com/'
        page = urlopen(url)
        soup = bs4(page, 'html.parser')
    
        aBox = soup.find_all('p', attrs={'class': 'money-text'})
        
        Token.Us = aBox[0].text.strip() # North America
        Token.Eu = aBox[1].text.strip() # Europe
        Token.Ch = aBox[2].text.strip() # China
        Token.Kr = aBox[3].text.strip() # Korean
        Token.Tw = aBox[4].text.strip() # Taiwan

        return True

    except Exception as e:
        print (Token.Date+' - '+Token.Time+' Problem in setToken()!')
        print ('Exception: ',e)

        return e

def main():
    
    attempt = 0
    isTrying = True
    while isTrying:

        attempt +=1

        date = datetime.now().strftime("%m/%d/%Y")
        time = datetime.now().strftime("%H:%M:%S")       

        if setToken(Token):

            isTrying = False
        else:
            
            print (date + ' - ' + time +' - setToken() failed, attempt', attempt ,'- Sleeping 30s...')
            t.sleep(30)   

        if attempt >5:

            print (date + ' - ' + time +' - setToken() failed, breaking')    
            isTrying = False

    attempt = 0
    isTrying = True
    while isTrying:

        attempt +=1

        date = datetime.now().strftime("%m/%d/%Y")
        time = datetime.now().strftime("%H:%M:%S")       

        if setCurrency(Currency):

            isTrying = False
        else:
            
            print (date + ' - ' + time +' - setCurrency() failed, attempt', attempt ,'- Sleeping 30s...')
            t.sleep(30)   

        if attempt >5:

            print (date + ' - ' + time +' - setCurrency() failed, breaking')    
            isTrying = False

    insertData(Token, Currency)

    conn.close()

main()
