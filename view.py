from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

def plot_graph_1(data):
    plt.plot(data, linewidth=2.0)   
    plt.show()

def plot_graph_2(data1, data2):
    plt.plot(data1, 'r')
    plt.plot(data2, 'b')
    plt.xlabel('Date Time')
    plt.ylabel('Value (0 - 1)')
    plt.legend()
    plt.show()

def plot_graph_3(data1, data2, data3):
    plt.plot(data1, 'r')
    plt.plot(data2, 'b')
    plt.plot(data3, 'g')
    plt.xlabel('Date Time')
    plt.ylabel('Value (0 - 1)')
    plt.legend()
    plt.show()