from data import database as db     # personal script
import analytics as anl             # personal script
import database                     # personal script

from datetime import datetime as dt
import pandas as pd
import view
import os

if __name__ == '__main__': 
    t_before = dt.now()
    # data collected in server
    dfWowtoken = database.read_Data('wowtoken')
    dfCurrency = database.read_Data('currency')
    df = database.join_data(dfCurrency, dfWowtoken)
    
    op = 1
    size = 1000

    if op == 1:
        data1 = df['Us']
        data1_name = 'Us'
        data2 = df['Brl']
        data2_name = 'Brasil'

    elif op == 2:
        data1 = df['Eu']
        data1_name = 'Europe'
        data2 = df['Eur']
        data2_name = 'Euro'

    elif op == 3:
        data1 = df['Ch']
        data1_name = 'China'
        data2 = df['Cny']
        data2_name = 'Renminbi'
    
    elif op == 4:
        data1 = df['Kr']
        data1_name = 'Korea'
        data2 = df['Krw']
        data2_name = 'Won Sul-coreano'

    # Data manipulation
    data1_nm = database.set_Normalized_Field(data1)
    data2_nm = database.set_Normalized_Field(data2) 

    data1_avg = database.set_Avg_Field(data1_nm)
    data2_avg = database.set_Avg_Field(data2_nm)

    predict_values = 5000
    data1_pred = anl.arma(data1_avg, predict_values)

    # Showing results
    t_after = dt.now()
    print('Elapsed time: '+str(t_after - t_before))
    print('Server: '+ data1_name)
    print('Currency: '+ data2_name)

    print('\nReal values')
    print('Correlation:', anl.correlationIndex(data1, data2))
    print('Covariance:', anl.covarianceIndex(data1, data2))     

    print('\nNormalized values')
    print('Correlation:', anl.correlationIndex(data1_nm, data2_nm))
    print('Covariance:', anl.covarianceIndex(data1_nm, data2_nm))

    print('\nAvarage values')
    print('Correlation:', anl.correlationIndex(data1_avg, data2_avg))
    print('Covariance:', anl.covarianceIndex(data1_avg, data2_avg))

    print('\nCalculated')
    print('Correlation:', anl.correlationIndex(data1_avg, data1_pred))
    print('Covariance:', anl.covarianceIndex(data1_avg, data1_pred))   
    
    view.plot_graph(data1_avg, 'True data', data1_pred, 'Data Predicted')  
