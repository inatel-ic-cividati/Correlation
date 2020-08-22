import analytics as an             # personal script
import database  as db             # personal script
import view      as vw             # personal script

from datetime import datetime as dt
import pandas as pd
import numpy as np
import os

if __name__ == '__main__': 
    t_before = dt.now()
    # data collected in server
    dfWowtoken = db.read_Csv('wowtoken_price_in_gold')
    dfCurrency = db.read_Csv('currency')
    df_original = db.join_data(dfCurrency, dfWowtoken)

    df_original['date'] = df_original['date_x']
    df_original['date'] = pd.to_datetime(df_original['date'], infer_datetime_format=True)

    df_original.set_index(df_original['date'], inplace=True)
    df_original.drop(columns=['date_x','date_y','date'], axis=1, inplace=True)
    
    # A ideia é usarmos de 01/07/19 até 30/06/20
    df = df_original
    #print(df['date']['2019/03/27'])

    wowtoken = np.array([
        db.set_Normalized_Field(df['Us']),
        db.set_Normalized_Field(df['Eu']),
        db.set_Normalized_Field(df['Ch']),
        db.set_Normalized_Field(df['Kr'])])

    currency = np.array([
        db.set_Normalized_Field(df['Brl']),
        db.set_Normalized_Field(df['Eur']),
        db.set_Normalized_Field(df['Cny']),
        db.set_Normalized_Field(df['Krw'])])

    p = np.array([
        an.pearson(wowtoken[0], currency[0]),
        an.pearson(wowtoken[1], currency[1]),
        an.pearson(wowtoken[2], currency[2]),
        an.pearson(wowtoken[3], currency[3])])
    
    k = np.array([
        an.kendall(wowtoken[0], currency[0]),
        an.kendall(wowtoken[1], currency[1]),
        an.kendall(wowtoken[2], currency[2]),
        an.kendall(wowtoken[3], currency[3])])

    s = np.array([
        an.spearman(wowtoken[0], currency[0]),
        an.spearman(wowtoken[1], currency[1]),
        an.spearman(wowtoken[2], currency[2]),
        an.spearman(wowtoken[3], currency[3])])

    # Showing results
    t_after = dt.now()
    #print('Elapsed time: '+str(t_after - t_before))
    print('start at:',df.index[0])
    print('end at:  ',df.index[-1])
    print('time interval:',df.index[-1] - df.index[0])
    print('')
    print( '| Region  | Currency | Pearson | Kendall | Spearman |')
    print(f'| America |    BRL   |  {p[0]}    {k[0]}     {s[0]} ')
    print(f'| Europe  |    Eur   |  {p[1]}    {k[1]}     {s[1]}   ')
    print(f'| China   |    Cny   |  {p[2]}    {k[2]}     {s[2]}   ')
    print(f'| Corea   |    Krw   |  {p[3]}    {k[3]}     {s[3]}   ')
 
    # synthesizing the results into a dataframe
    pd_s1 = pd.Series(['America','BRL',p[0], k[0], s[0]]).T
    pd_s2 = pd.Series(['Europe','Eur',p[1], k[1], s[1]]).T
    pd_s3 = pd.Series(['China','Cny',p[2], k[2], s[2]]).T
    pd_s4 = pd.Series(['Corea','Krw',p[3], k[3], s[3]]).T
    # Creating the dataframe
    final_result = pd.DataFrame(data=[pd_s1, pd_s2, pd_s3, pd_s4])
    mapa = {0:'Region', 1:'Currency', 2:'Pearson', 3:'Kendall', 4:'Spearman'}
    final_result.rename(columns=mapa, inplace=True)
    final_result['start'][0] =  df.index[0]
    final_result['end'][0] = df.index[-1]
    final_result.to_csv('correlation_result.csv')