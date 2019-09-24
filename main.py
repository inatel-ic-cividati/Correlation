import database
import pandas as pd

# create the database with the tables
database.set_DataBase()

# get the data
dataUs = database.get_Data('us')
dataEu = database.get_Data('eu')
dataChina = database.get_Data('china')
dataKorea = database.get_Data('korea')
dataTaiwan = database.get_Data('taiwan')
print()
data = [dataUs, dataEu, dataChina, dataKorea, dataTaiwan]

for i in data:
    i = database.unix_datetime(i)
    i = database.set_Avg_Field(i)
    i = database.set_Normalized_Field(i)

# insert into database
database.insert_Table(dataUs, 'wowtoken_us')
database.insert_Table(dataEu, 'wowtoken_eu')
database.insert_Table(dataChina, 'wowtoken_china')
database.insert_Table(dataKorea, 'wowtoken_korea')
database.insert_Table(dataTaiwan, 'wowtoken_taiwan')
