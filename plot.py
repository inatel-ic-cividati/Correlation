import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
 
conn = sqlite3.connect('wow.db')
query = 'SELECT * FROM wowtoken WHERE id <= 20 and Us != "";'
df = pd.read_sql_query(query,conn)
df = df(index = df['date'])

def convertStrFlt(dataFrame, name):
    
    # converting str to float
    dataFrame[name] = dataFrame[name].str.replace(',','.')
    dataFrame[name] = dataFrame[name].astype('float')
    df = dataFrame

convertStrFlt(df, 'Us')
convertStrFlt(df, 'Eu')
convertStrFlt(df, 'Ch')
convertStrFlt(df, 'Tw')
convertStrFlt(df, 'Kr')

print (df)
fmri = sns.load_dataset("fmri")
#print(fmri)
#sns.lineplot(data=fmri,palette="tab10",linewidth=2.5)
#g = sns.regplot(x="date", y="Us", data=df)
#g = sns.relplot(x="timepoint", y="signal", hue="event", style="event", col="region",kind="line", data=fmri)
g.fig.autofmt_xdate()
plt.show()
