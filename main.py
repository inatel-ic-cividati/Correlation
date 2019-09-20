import database

#database.set_DataBase()
dataUs = database.get_Data('us')
dataEu = database.get_Data('eu')
dataChina = database.get_Data('china')
dataKorea = database.get_Data('korea')
dataTaiwan = database.get_Data('taiwan')

database.insert_Table(dataUs, 'wowtoken_us')
database.insert_Table(dataEu, 'wowtoken_eu')
database.insert_Table(dataChina, 'wowtoken_china')
database.insert_Table(dataKorea, 'wowtoken_korea')
database.insert_Table(dataTaiwan, 'wowtoken_taiwan')

#print(dataUs)
