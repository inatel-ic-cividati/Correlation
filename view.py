import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# PARAMETERS
sampleColor1 = '#FF0000'
sampleColor2 = '#FF0000'
sampleColor3 = '#0000FF'
sampleColor4 = '#0000FF'

def plot_one(dfWowtoken, dfCurrency, label = 'Default'):
    # PLOT ONE
    label_avg = label + '_avg'
    fig1, allData = plt.subplots(2, 1, sharex = True)
    avgData1 = allData[0].twinx()
    avgData2 = allData[1].twinx()
    allData[0].plot(dfWowtoken[label], label=label, color = sampleColor1)
    allData[0].set_ylabel('WowToken ' + label +' value', color = sampleColor1)
    
    avgData1.plot(dfCurrency[label], label=label, color = sampleColor3)
    avgData1.set_ylabel('Currecny ' + label +' value', color = sampleColor3)

    # Plot all data with smoothing
    allData[1].plot(dfWowtoken[label_avg], label=label, color = sampleColor1)
    allData[1].set_ylabel('WowToken ' + label +' avg value', color = sampleColor1)  

    avgData2.plot(dfCurrency[label_avg], label=label, color = sampleColor3)
    avgData2.set_ylabel('Currecny ' + label +' avg value', color = sampleColor3)

    plt.show()

def plot_two(dfWowtoken, dfCurrency, label = 'Default'):
    # PLOT TWO
    label_avg = label + 'avg'
    fig2, axs = plt.subplots(2,1, sharex = True)

    wowTokenPlot = axs[0].twinx()
    wowTokenPlot.plot(dfWowtoken[label], color = sampleColor2)
    wowTokenPlot.set_ylabel('WowToken ' + label + ' Real', color = sampleColor2)
    axs[0].plot(dfWowtoken[label_avg], color = sampleColor4)
    axs[0].set_ylabel('WowToken ' +label + ' AVG', color = sampleColor4)

    labelPlot = axs[1].twinx()
    labelPlot.plot(dfCurrency[label],color = sampleColor1)
    labelPlot.set_ylabel('label '+ label +' Real', color=sampleColor1)
    axs[1].plot(dfCurrency[label_avg], color = sampleColor3)
    axs[1].set_ylabel('label '+ label +' AVG', color = sampleColor3)

    plt.show()

def plot_three(dfWowtoken, dfCurrency, label = 'Default'):
    # PLOT THREE
    label_avg = label + '_avg'
    fig, axs = plt.subplots(2,2,sharex = True)
    axs[0][0].set_title('WowToken '+ label + ' Real', color = sampleColor2)
    axs[0][0].plot(dfWowtoken[label], color = sampleColor2)

    axs[0][1].set_title('WowToken ' + label + ' AVG', color = sampleColor4)
    axs[0][1].plot(dfWowtoken[label_avg], color = sampleColor4)
    
    axs[1][0].set_title('label ' + label + ' Real', color=sampleColor1)
    axs[1][0].plot(dfCurrency[label],color = sampleColor1)

    axs[1][1].set_title('label '+label +' AVG', color = sampleColor3)
    axs[1][1].plot(dfCurrency[label_avg], color = sampleColor3)

    plt.show()    
