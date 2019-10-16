import numpy as np
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.arima_model import ARMA
import statsmodels.api as sm

def correlationIndex (array1, array2):
    # correlate the two arrays
    if len(array1) != len(array2):
        print('error in lenght')
        return

    else:
        cor = np.corrcoef(array1, array2, rowvar = False)
        cor = cor[0,1]
        # return the correlation index
        return cor

def autoregressive(array, qt = 0):
    # makes a autoregreesion
    model = AR(array)
    model_fit = model.fit()
    yhat = model_fit.predict(len(array), len(array)+qt)
    # return the array preditcted
    return yhat

def arima(array, qt = 0):
    # Autoregressive Moving Average ARMA(p,q) Model
    model = ARMA(array, (1,0))
    model_fit = model.fit()
    yhat = model_fit.predict(len(array), len(array)+qt)

    return yhat