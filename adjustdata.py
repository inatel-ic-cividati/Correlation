import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.metrics import r2_score
from sklearn.preprocessing import Normalizer
from sklearn import preprocessing 
import sklearn

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
    # define date and time as index
    dataFrame.index = dataFrame['date']

    return dataFrame

def setAvgField(dataFrame, name, rollingNumber = 400):
    # create average field in the dataframe
    dataFrame[name + '_avg'] = dataFrame[name].rolling(rollingNumber).mean()

    return dataFrame

def setNormalizeField(dataFrame, name):
    # normalize the data
    # divide the whole colomn by the max index
    dataFrame[name + '_nm'] = dataFrame[name] / max(dataFrame[name])

    return dataFrame

def main():
    # opening the database
    conn = sqlite3.connect('C:/Users/Amor/Desktop/IC/wow.db')
    cursor = conn.cursor()

    # setting up the wowtoken dataframe
    query = 'SELECT * FROM wowtoken WHERE Us != "";'
    dfWowtoken = pd.read_sql_query(query,conn)

    # creating a new index in the dataframe
    convertStrDate(dfWowtoken)
    dfWowtoken = dfWowtoken.drop(['time','id','date'], axis = 1)

    # creating new columns in the dataframe
    for column in dfWowtoken.columns:
        convertStrFlt(dfWowtoken, column)
        setAvgField(dfWowtoken,column)
        setNormalizeField(dfWowtoken,column)

    # setting up the currency dataframe
    query = 'SELECT * FROM currency WHERE date != "";'
    dfCurrency = pd.read_sql_query(query,conn)

    # creating a new index in the dataframe
    convertStrDate(dfCurrency)
    dfCurrency = dfCurrency.drop(['time','id','date'], axis = 1)

    # creating new columns in the dataframe
    for column in dfCurrency.columns:
        convertStrFlt(dfCurrency, column)
        setAvgField(dfCurrency, column)
        setNormalizeField(dfCurrency, column)

    # creating the new database
    conn = sqlite3.connect('C:/Users/Amor/Desktop/IC/wow_az.db')

    # writing in the database
    dfWowtoken.to_sql('wowtoken', conn)
    dfCurrency.to_sql('currency', conn)

    # closing the connection
    conn.close()

main()
