from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.ar_model import AR
from scipy.stats import pearsonr
import statsmodels.api as sm
import numpy as np

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

def ar(array, qt = 0):
    # makes a autoregreesion
    model = AR(array)
    model_fit = model.fit()
    yhat = model_fit.predict(len(array), len(array)+qt-1)
    
    return yhat

def arma(array, qt = 0):
    # Autoregressive Moving Average ARMA(p,q) Model
    model = ARMA(array, (1,0))
    model_fit = model.fit()
    yhat = model_fit.predict(len(array), len(array)+qt)
    
    return yhat
