from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.ar_model import AR
from scipy.stats import pearsonr
import statsmodels.api as sm
import pandas as pd
import numpy as np

def joinData(array, yhat): 
    # Joining the original data with the calculated data
    myList = list(array[len(array)-len(yhat):].index.values)
    yhat.index = (myList)
    
    dfNew = pd.concat([array[:-len(yhat)], yhat])
    
    return dfNew
    
def correlationIndex(array1, array2):
    # correlate the two arrays
    if len(array1) != len(array2):
        print('error in lenght')
        return

    else:
        cor = np.corrcoef(array1, array2, rowvar = False)[0,1]*100
        # return the correlation index
        cor =  str("%.2f" % cor) +'%'
        return cor

def covarianceIndex(array1, array2):
    # covariance between two arrays
    if len(array1) != len(array2):
        print('error in lenght')
        return

    else:
        cov = np.cov(array1, array2)[0][1]*100
        # return the covariance index
        cov = str("%.2f" % cov) + '%'
        return cov

# p is the number of autoregressive terms
# d is the number of nonseasonal differences needed for stationarity
# q is the number of lagged forecast errors in the prediction equation

def ar(array, qt):
    # Autoregressive Model AR(p) 
    print('AUTOREGRESSIVE')
    model = AR(array)
    model_fit = model.fit(1)
    yhat = model_fit.predict(len(array)-qt,len(array)-1)
    dfNew = joinData(array, yhat)

    return dfNew

def arma(array, qt):
    # Autoregressive oving Avarage Model ARMA(p,q) 
    model = ARMA(array, (0,1))
    model_fit = model.fit()
    yhat = model_fit.predict(len(array)-qt,len(array)-1)
    dfNew = joinData(array, yhat)

    return dfNew

def arima(array, qt):
    # Autoregressive Integrated Moving Avarage Model ARIMA(p,q,d) 
    model = ARIMA(array, (0,0,1))
    model_fit = model.fit()
    yhat = model_fit.predict(len(array)-qt,len(array)-1)
    dfNew = joinData(array, yhat)

    return dfNew

