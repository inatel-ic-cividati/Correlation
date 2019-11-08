from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

def plot_graph_1(data):
    plt.plot(data, linewidth=2.0)   
    plt.show()

def plot_graph_2(data1, data2):
    plt.plot(data1, 'r')
    plt.plot(data2, 'b')
    plt.show()