import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.metrics import r2_score
#plt.style.use('dark_background')

def main():

    # setting up the databse
    db_url = 'C:/YOUR/FOLDER/HERE/'
    conn = sqlite3.connect(db_url+'wow_az.db')
    cursor = conn.cursor()

    # setting up wowtokne dataframe
    query = 'SELECT * FROM wowtoken WHERE Us != "";'
    dfWowtoken = pd.read_sql_query(query,conn)

    # setting up currecny dataframe
    query = 'SELECT * FROM currency WHERE date != "";'
    dfCurrency = pd.read_sql_query(query,conn)

    op = 2

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
        currency = 'Usd'
    
    # GET THE AVG VALUE OF WOWTOKEN
    # PARAMETERS
    sampleColor1 = '#FF0000'
    sampleColor2 = '#FF0000'
    sampleColor3 = '#0000FF'
    sampleColor4 = '#0000FF'

    country_avg = country + '_avg'
    currency_avg = currency + '_avg'

    # PLOT ONE
    # Plot all data without smoothing
    fig1, allData = plt.subplots(2, 1, sharex = True)
    avgData1 = allData[0].twinx()
    avgData2 = allData[1].twinx()

    allData[0].plot(dfWowtoken[country], label=country, color = sampleColor1)
    allData[0].set_ylabel('WowToken ' + country +' value', color = sampleColor1)
    
    avgData1.plot(dfCurrency[currency], label=currency, color = sampleColor3)
    avgData1.set_ylabel('Currecny ' + currency +' value', color = sampleColor3)

    # Plot all data with smoothing
    allData[1].plot(dfWowtoken[country_avg], label=country, color = sampleColor1)
    allData[1].set_ylabel('WowToken ' + country +' avg value', color = sampleColor1)  

    avgData2.plot(dfCurrency[currency_avg], label=currency, color = sampleColor3)
    avgData2.set_ylabel('Currecny ' + currency +' avg value', color = sampleColor3)

    # PLOT TWO
    fig2, axs = plt.subplots(2,1, sharex = True)

    wowTokenPlot = axs[0].twinx()
    wowTokenPlot.plot(dfWowtoken[country], color = sampleColor2)
    wowTokenPlot.set_ylabel('WowToken ' + country + ' Real', color = sampleColor2)
    axs[0].plot(dfWowtoken[country_avg], color = sampleColor4)
    axs[0].set_ylabel('WowToken ' +country + ' AVG', color = sampleColor4)

    currencyPlot = axs[1].twinx()
    currencyPlot.plot(dfCurrency[currency],color = sampleColor1)
    currencyPlot.set_ylabel('Currency '+ currency +' Real', color=sampleColor1)
    axs[1].plot(dfCurrency[currency_avg], color = sampleColor3)
    axs[1].set_ylabel('Currency '+ currency +' AVG', color = sampleColor3)

    # PLOT THREE
    fig, axs = plt.subplots(2,2,sharex = True)
    axs[0][0].set_title('WowToken '+ country + ' Real', color = sampleColor2)
    axs[0][0].plot(dfWowtoken[country], color = sampleColor2)

    axs[0][1].set_title('WowToken ' + country + ' AVG', color = sampleColor4)
    axs[0][1].plot(dfWowtoken[country_avg], color = sampleColor4)
    
    axs[1][0].set_title('Currency ' + currency + ' Real', color=sampleColor1)
    axs[1][0].plot(dfCurrency[currency],color = sampleColor1)

    axs[1][1].set_title('Currency '+currency +' AVG', color = sampleColor3)
    axs[1][1].plot(dfCurrency[currency_avg], color = sampleColor3)

    plt.show()    
    
main()
