from data import database as db     # personal script
import analytics as anl             # personal script
import database                     # personal script

import pandas as pd
import view
import os

def main_not_finished():
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

if __name__ == '__main__': 

    # data collected in server
    dfWowtoken = database.read_Data('wowtoken')
    dfCurrency = database.read_Data('currency')
    df = database.join_data(dfCurrency, dfWowtoken)
    
    op = 2

    if op == 1:
        data1 = df['Us']
        data2 = df['Brl']

    elif op == 2:
        data1 = df['Eu']
        data2 = df['Eur']

    elif op == 3:
        data1 = df['Ch']
        data2 = df['Cny']
    
    elif op == 4:
        data1 = df['Kr']
        data2 = df['Krw']

    print('\nReal values')
    print('Correlation:', anl.correlationIndex(data1, data2))
    print('Covariance:', anl.covarianceIndex(data1, data2))

    data1_nm = database.set_Normalized_Field(data1)
    data2_nm = database.set_Normalized_Field(data2)  

    print('\nNormalized values')
    print('Correlation:', anl.correlationIndex(data1_nm, data2_nm))
    print('Covariance:', anl.covarianceIndex(data1_nm, data2_nm))

    data1_avg = database.set_Avg_Field(data1_nm)
    data2_avg = database.set_Avg_Field(data2_nm)

    print('\nAvarage values')
    print('Correlation:', anl.correlationIndex(data1_avg, data2_avg))
    print('Covariance:', anl.covarianceIndex(data1_avg, data2_avg))

    view.plot_graph_2(data1_avg, data2_avg)
