    import matplotlib.pyplot as plt
    from sklearn.metrics import r2_score
    import numpy as np

    def plot_graph_1(data):
        plt.plot(data, linewidth=2.0)   
        plt.show()

    def plot_graph_2(x, y):

        # plot with various axes scales
        fig, axs = plt.subplots(2, sharex=True)
        fig.subplots_adjust(left=0.08, right=0.98, wspace=0.3)

        # linear
        ax = axs[0]
        ax.plot(x, y)
        ax.grid(True)

        # log
        ax = axs[1]
        ax.plot(x, y)
        ax.grid(True)

        plt.show()
