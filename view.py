from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_graph(data1, data2, data1_name='',data2_name='', details =''):

    fig, ax = plt.subplots()
    # legends and colors
    ax.plot(data2, color='#d7191c', label=data2_name) # ls=--
    ax.plot(data1, color='#2b83ba', label=data1_name)
    ax.grid()
    # position of the legend
    ax.legend(loc='best', shadow=True, fontsize='large')
    ax.set_title(data1_name+' e '+data2_name)
    # X legend and Y legend
    plt.xlabel('Data')
    plt.ylabel('Valor normalizado')
    
    plt.show()