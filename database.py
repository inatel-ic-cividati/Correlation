import sqlite3
import os
from data import database as db
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
            print(wowtokentable + " error: ", e)

def insert_Table(df, wowtokentable):
    # unfinished


def get_Data(wowtoken):
    # implements to get all tokens
    req = requests.get('https://wowtokenprices.com/history_prices_full.json')
    resp = req.text
    json_obj = json.loads(resp)
    data = pd.DataFrame(json_obj['us'])
    
    return data

get_Data('us')
