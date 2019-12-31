from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_graph(data1, data1_label, data2, data2_label):
    plt.plot(data1, 'black')
    plt.plot(data2, 'red')

    plt.xlabel('Date Time')
    plt.ylabel('Value (0 - 1)')
    plt.legend({data1_label, data2_label})
    
    plt.show()