import pandas_datareader as pdr

data = pdr.fred.FredReader("DEXUSEU",'2019-03-01','2019-03-13', freq='Daily')

print(data.read())
