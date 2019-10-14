import numpy as np
from statsmodels.tsa.ar_model import AR

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

def autoRegression(array):
    # makes a autoregreesion
    model = AR(array)
    model_fit = model.fit()

    yhat = model_fit.predict(len(array), len(array))
    # return the array preditcted
    return yhat
