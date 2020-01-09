from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_graph(data1, data2, server='', currency='', details =''):

    fig, ax = plt.subplots()
    # legends and colors
    ax.plot(data2, color='blue', label='Calculated Data', ls='--')
    ax.plot(data1, color='black', label='True Data')
    # position of the legend
    ax.legend(loc='upper left', shadow=True, fontsize='large')
    ax.set_title(server+' - '+currency+'\n'+details)
    # X legend and Y legend
    plt.xlabel('Date-Time')
    plt.ylabel('Variation (0 - 1)')
    
    plt.show()