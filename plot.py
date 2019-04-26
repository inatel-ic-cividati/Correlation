import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
sns.set_palette("husl")
 
def convertStrFlt(dataFrame, name):
    
    # converting str to float
    dataFrame[name] = dataFrame[name].str.replace(',','.')
    dataFrame[name] = dataFrame[name].astype('float')
    df = dataFrame

def convertStrDate(dataFrame):

    # converting the column date to datetime64
    dataFrame['date'] = dataFrame['date'].str.replace('/','-')
    dataFrame['date'] = dataFrame['date']+' '+dataFrame['time']
    dataFrame['date'] = dataFrame['date'].astype('datetime64[s]')
    dataFrame.index = dataFrame['date']

    df = dataFrame

def main():

    conn = sqlite3.connect('wow.db')
    query = 'SELECT * FROM wowtoken WHERE id <= 50 and Us != "";'
    df = pd.read_sql_query(query,conn)

    convertStrFlt(df, 'Us')
    convertStrFlt(df, 'Eu')
    convertStrFlt(df, 'Ch')
    convertStrFlt(df, 'Tw')
    convertStrFlt(df, 'Kr')
    convertStrDate(df)
    #df = df.drop(['time','id'], axis = 1)
    
    g1 = sns.regplot(x='date',y='Us',data=df, fit_reg=True)
    g1.set(xlabel='time', ylabel='value',title='Wow token value')
    plt.show()
    
    
main()
