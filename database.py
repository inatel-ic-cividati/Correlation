from data import database as db # personal script
from datetime import datetime
import pandas as pd
import numpy as np
import requests
import sqlite3
import array
import json
import os

def set_DataBase():
    # creating the databse 
    try:
        conn = db.get_connection('wow.db')
        cursor = conn.cursor()

        params = ['us', 'eu', 'china', 'korea', 'taiwan']

        for table in params:
            set_Table('wowtoken_'+table, cursor)
            set_Table('currency_'+table, cursor)

        conn.close()

    except sqlite3.Error as e:
        print('error:',e)

def set_Table(Table, cursor): 
    try:
        # creating wowtoken table
        Colunm = Table.replace("wowtoken_","")
        Colunm = Colunm.replace("currency_","")

        cursor.execute("""
        CREATE TABLE """+Table+"""(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            time INT NOT NULL,
            """+Colunm+""" FLOAT NOT NULL
        );
        """)
        print(Table+' table created sucessfully!')

    except sqlite3.Error as e:
            print(Table, 'error:', e)

def get_Data(wowtoken):
    # get the data directly from wowtokenprices.com
    # with internet connection
    try:
        # load the data from the following link
        req = requests.get('https://wowtokenprices.com/history_prices_1_day.json')
        resp = req.text
        json_obj = json.loads(resp)
        data = pd.DataFrame(json_obj[wowtoken])
        print(wowtoken, 'data collected:', len(json_obj[wowtoken]))

    # with no internet connection
    except:
        path = db.get_db_path() 

        # load the data from file wowtoken_COUNTRY.json
        with open(path+'/wowtoken_'+wowtoken+'.json', 'r') as f:
            json_obj = json.load(f)
            data = pd.DataFrame(json_obj)
            print(wowtoken, 'data collected:', len(json_obj))

    # reorder columns showing time first than price
    data = data[['time', 'price']]
    return data

def read_Data(tableName):
    # read the data from the database 'wow_read.db'
    conn = db.get_connection('wow_read.db')

    if tableName == 'wowtoken':
        
        dataFrame = pd.read_sql_query('SELECT * FROM '+tableName+' WHERE us != ""', conn)
        
        dataFrame = str_Date(dataFrame)
        dataFrame = dataFrame.drop(columns=['index', 'id', 'date', 'time'], axis = 0)

        dataFrame = str_Float(dataFrame, 'Us')
        dataFrame = str_Float(dataFrame, 'Eu')
        dataFrame = str_Float(dataFrame, 'Ch')
        dataFrame = str_Float(dataFrame, 'Kr')
        dataFrame = str_Float(dataFrame, 'Tw')
        return dataFrame

    elif tableName == 'currency':
        
        dataFrame = pd.read_sql_query('SELECT * FROM '+tableName+' WHERE Brl != ""', conn)
        
        dataFrame = str_Date(dataFrame)
        dataFrame = dataFrame.drop(columns=['index', 'id', 'date', 'time'], axis = 0)

        dataFrame = str_Float(dataFrame, 'Usd')
        dataFrame = str_Float(dataFrame, 'Eur')
        dataFrame = str_Float(dataFrame, 'Cny')
        dataFrame = str_Float(dataFrame, 'Krw')
        dataFrame = str_Float(dataFrame, 'Brl')
        return dataFrame

def insert_Table(dataFrame, wowtokenTable):
    # insert dataframe into wowtokne table
    conn = db.get_connection('wow.db')
    dataFrame.to_sql(wowtokenTable, conn, if_exists='replace')

def unix_datetime(dataFrame):
    # convert unix to datetime
    # credits: Daniel Pontello
    dataFrame['time'] = dataFrame['time'].apply(lambda x: datetime.fromtimestamp(x))
    return dataFrame

def join_data(df1, df2):
    merge = pd.merge(df1,df2, left_index=True, right_index=True)
    return merge

def str_Float(dataFrame, columnName):
    # converting str to float
     # replace all ',' to '.'
    dataFrame[columnName] = dataFrame[columnName].str.replace(',','.')
    # convert the type of dataFrame['columnName] to flaot
    dataFrame[columnName] = dataFrame[columnName].astype('float')
    
    return dataFrame

def str_Date(dataFrame):
    # converting the column date to datetime64      
    # replace all '/' to '-'
    dataFrame['date'] = dataFrame['date'].str.replace('/','-')
    # agroup time and date
    dataFrame['date'] = dataFrame['date']+' '+dataFrame['time']
    # convert the type of dataFrame['date'] to datetime with precision in minuts
    dataFrame['date'] = dataFrame['date'].astype('datetime64[m]')
    # define date and time as index
    dataFrame.index = dataFrame['date']

    return dataFrame

def set_Avg_Field(data, rollingNumber = 400):
    # create average field in the dataframe
    # search more this function
    data = data.rolling(rollingNumber).mean()
    data = data[rollingNumber:]
    
    return data

def set_Normalized_Field(data):
    # normalize the data
    # divide the whole colomn by the max index
    data = data / max(data)

    return data