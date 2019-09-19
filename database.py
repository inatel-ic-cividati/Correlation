import sqlite3
import os
from data import database as db
import json
import requests
import array
import pandas as pd

def set_DataBase():
    # creating the databse 
    conn = db.get_connection('wow.db')
    cursor = conn.cursor()
    print('wow.db created sucessfully!')

    params = ['us', 'eu', 'china', 'korea', 'taiwan']

    for table in params:
        set_Table('wowtoken_'+table, cursor)
        set_Table('currency_'+table, cursor)

    conn.close()

def set_Table(tablewowtoken, cursor): 
    try:
        # creating wowtoken table
        colunmwowtoken = tablewowtoken.replace("wowtoken_","")
        colunmwowtoken = colunmwowtoken.replace("currency_","")

        cursor.execute("""
        CREATE TABLE """+tablewowtoken+"""(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            time INT NOT NULL,
            """+colunmwowtoken+""" FLOAT NOT NULL
        );
        """)
        print(tablewowtoken+' table created sucessfully!')

    except sqlite3.Error as e:
            print(tablewowtoken + " error: ", e)

def insert_Table(tuple, tablewowtoken):

    print('a')


def get_Data(wowtoken):
    #unfinished
    js = requests.get('https://wowtokenprices.com/history_prices_1_day.json')
    js = js.json()

    data = pd.DataFrame(columns={'us','eu'})

    for index in js['us']:
        print(index)

    print(data)

get_Data('us')
