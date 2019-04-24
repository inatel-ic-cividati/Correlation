import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
sns.set(style="darkgrid")
 


def convertStrFlt(dataFrame, name):
    
    # converting str to float
    dataFrame[name] = dataFrame[name].str.replace(',','.')
    dataFrame[name] = dataFrame[name].astype('float')
    df = dataFrame

def convertStrDate(dataFrame):

    # converting the column date to datetime64
    dataFrame['date'] = dataFrame['date'].str.replace('/','-')
    
    for i in dataFrame['date']:
        aStr = i.split('-')
        aD = aStr[1]
        aM = aStr[0]
        aY = aStr[2]
        i = aY +'-'+ aM + '-' + aD
        dataFrame['date'] = i
        pass

    dataFrame['date'] = dataFrame['date']+' '+dataFrame['time']
    dataFrame['date'] = dataFrame['date'].astype('datetime64[s]')

    dataFrame.index = dataFrame['date']
    dataFrame = dataFrame.drop(columns='time')
    dataFrame = dataFrame.drop(columns='id')
    dataFrame = dataFrame.drop(columns='date')
    df = dataFrame

def main():

    conn = sqlite3.connect('wow.db')
    query = 'SELECT * FROM wowtoken WHERE id <= 20 and Us != "";'
    df = pd.read_sql_query(query,conn)

    convertStrFlt(df, 'Us')
    convertStrFlt(df, 'Eu')
    convertStrFlt(df, 'Ch')
    convertStrFlt(df, 'Tw')
    convertStrFlt(df, 'Kr')
    convertStrDate(df)
    df = df.drop(columns='time')
    df = df.drop(columns='id')
    df = df.drop(columns='date')
    
    #print (df)
    
    g = sns.lineplot(data=df,palette='tab10',linewidth=2.5)


main()
