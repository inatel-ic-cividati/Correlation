from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.ar_model import AR

# Correlation models
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau

import statsmodels.api as sm
import pandas as pd
import numpy as np

def joinData(array, yhat): 
    # Joining the original data with the calculated data
    myList = list(array[len(array)-len(yhat):].index.values)
    yhat.index = (myList)
    
    dfNew = pd.concat([array[:-len(yhat)], yhat])
    
    return dfNew
     
def pearson(a1, a2):
    c_index = pearsonr(a1, a2)[0]
    c_index = "%.2f" % round(c_index, 2)
    return c_index

def kendall(a1, a2):
    c_index = kendalltau(a1, a2)[0]
    c_index = "%.2f" % round(c_index, 2)
    return c_index

def spearman(a1, a2):
    c_index = spearmanr(a1, a2)[0]
    c_index = "%.2f" % round(c_index, 2)
    return c_index

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

# autoregression anotations
# A good way to think about it is (AR, I, MA).
# p is the number of autoregressive terms
# d is the number of nonseasonal differences needed for stationarity
# q is the number of lagged forecast errors in the prediction equation

# VER DEPOIS https://stats.stackexchange.com/questions/44992/what-are-the-values-p-d-q-in-arima

def ar(array, qt):
    # Autoregressive Model AR(p) 
    model = AR(array)
    model_fit = model.fit()
    yhat = model_fit.predict(len(array)-qt,len(array)-1)
    dfNew = joinData(array, yhat)

    return dfNew

def arma(array, qt, p = 0, q = 1):
    # Autoregressive Moving Avarage Model ARMA(p,q) 
    model = ARMA(array, (p, q))
    model_fit = model.fit()
    yhat = model_fit.predict(len(array)-qt,len(array)-1)
    dfNew = joinData(array, yhat)

    return dfNew

def arima(array, qt, p = 0, q = 0, d = 1):
    # Autoregressive Integrated Moving Avarage Model ARIMA(p,q,d) 
    model = ARIMA(array, (p, q, d))
    model_fit = model.fit()
    yhat = model_fit.predict(len(array)-qt,len(array)-1)
    dfNew = joinData(array, yhat)

    return dfNew
