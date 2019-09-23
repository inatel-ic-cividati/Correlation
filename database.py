import sqlite3
import os
from data import database as db
from datetime import datetime
import json
import requests
import array
import pandas as pd

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

def set_Table(wowtokentable, cursor): 
    try:
        # creating wowtoken table
        wowtokencolunm = wowtokentable.replace("wowtoken_","")
        wowtokencolunm = wowtokencolunm.replace("currency_","")

        cursor.execute("""
        CREATE TABLE """+wowtokentable+"""(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            time INT NOT NULL,
            """+wowtokencolunm+""" FLOAT NOT NULL
        );
        """)
        print(wowtokentable+' table created sucessfully!')

    except sqlite3.Error as e:
            print(wowtokentable, 'error:', e)

def get_Data(wowtoken):
    
    # with internet connection
    try:
        req = requests.get('https://wowtokenprices.com/history_prices_1_day.json')
        resp = req.text
        json_obj = json.loads(resp)
        data = pd.DataFrame(json_obj[wowtoken])
        print(wowtoken, 'data collected:', len(json_obj[wowtoken]))

    # with no internet connection
    except:
        path = db.get_db_path() 

        with open(path+'/wowtoken_'+wowtoken+'.json', 'r') as f:
            json_obj = json.load(f)
            data = pd.DataFrame(json_obj)
            print(wowtoken, 'data collected:', len(json_obj))

    return data

def insert_Table(df, wowtokentable):

    conn = db.get_connection('wow.db')
    df.to_sql(wowtokentable, conn, if_exists='replace')

def unix_datetime(dataFrame):
    # convert unix to datetime
    timestamp = dataFrame['time']
    for i in range (0,len(dataFrame['price'])):
        dataFrame['time'][i] = datetime.fromtimestamp(timestamp[i])
    os.system('cls')
    return dataFrame

def str_Float(dataFrame, name):
    # converting str to float
    # replace all ',' to '.'
    dataFrame[name] = dataFrame[name].str.replace(',','.')
    # convert the type of dataFrame['name] to flaot
    dataFrame[name] = dataFrame[name].astype('float')
    
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

def set_Avg_Field(dataFrame, name, rollingNumber = 400):
    # create average field in the dataframe
    # search more this function
    dataFrame[name + '_avg'] = dataFrame[name].rolling(rollingNumber).mean()

    return dataFrame

def set_Normalized_Field(dataFrame, name):
    # normalize the data
    # divide the whole colomn by the max index
    dataFrame[name + '_nm'] = dataFrame[name] / max(dataFrame[name])

    return dataFrame

