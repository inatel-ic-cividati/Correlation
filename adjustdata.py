import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.metrics import r2_score
from sklearn.preprocessing import Normalizer
from sklearn import preprocessing 
import sklearn

db_url = 'C:/Your/Folder/here/'

# converting str to float
def convertStrFlt(dataFrame, name):
    # replace all ',' to '.'
    dataFrame[name] = dataFrame[name].str.replace(',','.')
    # convert the type of dataFrame['name] to flaot
    dataFrame[name] = dataFrame[name].astype('float')
    
    return dataFrame

# converting the column date to datetime64
def convertStrDate(dataFrame):
    # replace all '/' to '-'
    dataFrame['date'] = dataFrame['date'].str.replace('/','-')
    # agroup time and date
    dataFrame['date'] = dataFrame['date']+' '+dataFrame['time']
    # convert the type of dataFrame['date'] to datetime with precision in minuts
    dataFrame['date'] = dataFrame['date'].astype('datetime64[m]')
    # define date and time as index
    dataFrame.index = dataFrame['date']

    return dataFrame

# create average field in the dataframe
def setAvgField(dataFrame, name, rollingNumber = 400):
    dataFrame[name + '_avg'] = dataFrame[name].rolling(rollingNumber).mean()

    return dataFrame

# normalize the data
def setNormalizeField(dataFrame, name):
    # divide the whole colomn by the max index
    dataFrame[name + '_nm'] = dataFrame[name] / max(dataFrame[name])

    return dataFrame

def main():
        
    # opening the database
    conn = sqlite3.connect(db_url+'wow.db')

    # setting up the wowtoken dataframe
    query = 'SELECT * FROM wowtoken WHERE Us != "";'
    dfWowtoken = pd.read_sql_query(query,conn)

    # creating a new index in the dataframe
    convertStrDate(dfWowtoken)
    dfWowtoken = dfWowtoken.drop(['time','id','date', 'index'], axis = 1)

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
    dfCurrency = dfCurrency.drop(['time','id','date', 'index'], axis = 1)

    # creating new columns in the dataframe
    for column in dfCurrency.columns:
        convertStrFlt(dfCurrency, column)
        setAvgField(dfCurrency, column)
        setNormalizeField(dfCurrency, column)

    # creating the new database
    conn = sqlite3.connect(db_url+'wow_az.db')

    
    # Re-ordering columns 
    dfCurrency = dfCurrency.reindex(sorted(dfCurrency.columns), axis=1)
    dfWowtoken = dfWowtoken.reindex(sorted(dfWowtoken.columns), axis=1)
    
    # writing in the database
    dfWowtoken.to_sql('wowtoken', conn)
    dfCurrency.to_sql('currency', conn)

    # closing the connection
    conn.close()

main()
