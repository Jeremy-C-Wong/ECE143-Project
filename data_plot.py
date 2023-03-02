import matplotlib.pyplot as plt
import pandas
import csv
import pandas as pd
import time
import numpy as np

'''
TO-DO : Follow the peak graph style
and number of rows : once combined_new is resolved 
'''

plt.rcParams["figure.figsize"] = [15.00, 5.00]
plt.rcParams["figure.autolayout"] = True

#plot 1 STATIC: Netflix vs Amazon prime , DL_RATE VS Time 
columns = ['Day_Timeframe','DL_bitrate','RSRQ']

df1 = pd.read_csv("./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv", usecols=columns)
df2 = pd.read_csv("./5Gdataset-master/Netflix/Static/Season3-StrangerThings/combined.csv", usecols= columns)


ax = df1.plot(x='Day_Timeframe',y='DL_bitrate')
df2.plot(ax=ax,x='Day_Timeframe',y='DL_bitrate')
plt.savefig('plot1.png')


#plot 2 Driving:  Netflix vs Amazon prime , DL_RATE VS Time 

df3 = pd.read_csv("./5Gdataset-master/Amazon_Prime/Driving/Season3-TheExpanse/combined.csv", usecols=columns)
df4 = pd.read_csv("./5Gdataset-master/Netflix/Driving/Season3-StrangerThings/combined.csv", usecols= columns)


ax = df3.plot(x='Timestamp',y='DL_bitrate')
df4.plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.savefig('plot2.png')


#plot 3 Static vs Driving: Amazon prime,
# DL_RATE VS Time

ax = df1.plot(x='Timestamp',y='DL_bitrate')

df3.plot(ax=ax,x='Timestamp',y='DL_bitrate')
plt.legend(['Static','Driving'])
plt.savefig('plot3.png')

#plot 4 Static vs Driving: NETFLIX,
#DL_RATE VS Time

ax = df2.plot(x='Timestamp',y='DL_bitrate')

df4.plot(ax=ax,x='Timestamp',y='DL_bitrate')
plt.legend(['Static','Driving'])
plt.savefig('plot4.png')

#plot 5 Static vs Driving: Amazon prime,
# RSRQ VS Time
Indices3 = np.where(df3['RSRQ'] == '-')[0]
Indices4 = np.where(df4['RSRQ'] == '-')[0]

for i in Indices3:
    df3 = df3.drop(i)

for i in Indices4:
    df4 = df4.drop(i)


plt.ylim(-40,0)
ax = df3.plot(x='Timestamp',y='RSRQ')

df1.plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Static','Driving'])
plt.savefig('plot5.png')

#plot 6 Static vs Driving: NETFLIX,
# RSRQ VS Time

plt.ylim(-40,0)

ax = df4.plot(x='Timestamp',y='RSRQ')

df2.plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Static','Driving'])
plt.savefig('plot6.png')
