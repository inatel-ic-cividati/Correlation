from data import database as db     # personal script
import analytics as anl             # personal script
import database                     # personal script

from datetime import datetime as dt
import pandas as pd
import view
import os

def alternative_main():
    # create the database with the tables
    database.set_DataBase()
    os.system('cls')

    # get the data
    dataUs = database.get_Data('us')
    dataEu = database.get_Data('eu')
    dataChina = database.get_Data('china')
    dataKorea = database.get_Data('korea')
    dataTaiwan = database.get_Data('taiwan')
    os.system('cls')

    data = [dataUs, dataEu, dataChina, dataKorea, dataTaiwan]

    for i in data:
        i = database.unix_datetime(i)
        i = database.set_Avg_Field(i)
        i = database.set_Normalized_Field(i)
        i = i.reindex(sorted(i.columns), axis = 1)

    # insert into database
    database.insert_Table(dataUs, 'wowtoken_us')
    database.insert_Table(dataEu, 'wowtoken_eu')
    database.insert_Table(dataChina, 'wowtoken_china')
    database.insert_Table(dataKorea, 'wowtoken_korea')
    database.insert_Table(dataTaiwan, 'wowtoken_taiwan')
    os.system('cls')

    print('Your data is sotored in /data/wow.db!')
    print(dataEu['price'])