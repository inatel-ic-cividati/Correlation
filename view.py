from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_graph(data1, data2, data1_name='',data2_name='', details =''):

    fig, ax = plt.subplots()
    # legends and colors
    ax.plot(data2, color='blue', label=data2_name) # ls=--
    ax.plot(data1, color='black', label=data1_name)
    # position of the legend
    ax.legend(loc='lower left', shadow=True, fontsize='large')
    ax.set_title(data1_name+' - '+data2_name+'\n'+details)
    # X legend and Y legend
    plt.xlabel('Date-Time')
    plt.ylabel('Variation (0 - 1)')
    
    plt.show()