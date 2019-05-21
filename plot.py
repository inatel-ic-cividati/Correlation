import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('dark_background')
 
def convertStrFlt(dataFrame, name):
    
    # converting str to float
    dataFrame[name] = dataFrame[name].str.replace(',','.')
    dataFrame[name] = dataFrame[name].astype('float')
    
    return dataFrame

def convertStrDate(dataFrame):

    # converting the column date to datetime64
    dataFrame['date'] = dataFrame['date'].str.replace('/','-')
    dataFrame['date'] = dataFrame['date']+' '+dataFrame['time']
    dataFrame['date'] = dataFrame['date'].astype('datetime64[m]')
    dataFrame.index = dataFrame['date']

    return dataFrame

def main():

    conn = sqlite3.connect('wow.db')
    cursor = conn.cursor()

    # SETTING UP WOWTOKEN DATA FRAME
    query = 'SELECT * FROM wowtoken WHERE Us != "";'
    dfWowtoken = pd.read_sql_query(query,conn)
    
    dfWowtoken = convertStrFlt(dfWowtoken, 'Us')
    dfWowtoken = convertStrFlt(dfWowtoken, 'Eu')
    dfWowtoken = convertStrFlt(dfWowtoken, 'Ch')
    dfWowtoken = convertStrFlt(dfWowtoken, 'Tw')
    dfWowtoken = convertStrFlt(dfWowtoken, 'Kr')
    dfWowtoken = convertStrDate(dfWowtoken)
    dfWowtoken = dfWowtoken.drop(['time','id','date'], axis = 1)

    # SETTING UP CURRENCY DATA FRAME
    query = 'UPDATE currency SET Brl="0" WHERE Brl IS NULL;'
    cursor.execute(query)

    query = 'SELECT * FROM currency;'
    dfCurrency = pd.read_sql_query(query,conn)

    convertStrFlt(dfCurrency,'Usd')
    convertStrFlt(dfCurrency,'Eur')
    convertStrFlt(dfCurrency,'Cny')
    convertStrFlt(dfCurrency,'Krw')
    convertStrFlt(dfCurrency,'Brl')
    convertStrDate(dfCurrency)

    print(dfCurrency)
    dfCurrency = dfCurrency.drop(['time','id','date'], axis = 1)

    # PARAMS
    yColor = '#00FFFF' # #00FFFF -> BLUE
    xColor = '#FF1493' # #FF1493 -> PINK
    xRotation = 20

    op = 1

    if op == 0:
        country = 'Us'
        currency = 'Usd'
    elif op == 1:
        country = 'Eu'
        currency = 'Eur'
    elif op == 2:
        country = 'Ch'
        currency = 'Cny'
    elif op == 3:
        country = 'Kr'
        currency = 'Krw'
    elif op == 4:
        country = 'Eu'
        currency = 'Brl'

    plt.subplot(2,1,1)
    plt.plot(dfWowtoken[country], label=country, color = yColor)
    plt.xlabel('Time', color = xColor)
    plt.xticks(rotation = xRotation, color = xColor)
    plt.yticks(color = yColor)
    plt.ylabel('Value', color = yColor)
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(dfCurrency[currency], label=currency, color = yColor)
    plt.xlabel('Time', color = xColor)
    plt.xticks(rotation = xRotation, color = xColor)
    plt.yticks(color = yColor)
    plt.ylabel('Value', color = yColor)
    plt.legend()
  
    plt.show()    
    
main()
