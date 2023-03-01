import matplotlib.pyplot as plt
import pandas
import csv
import pandas as pd
import time

'''
TO-DO : Follow the peak graph style
and number of rows : once combined_new is resolved 

'''


plt.rcParams["figure.figsize"] = [15.00, 5.00]
plt.rcParams["figure.autolayout"] = True

#plot 1 STATIC: Netflix vs Amazon prime , DL_RATE VS Time 
columns = ['Timestamp','DL_bitrate','RSRQ','RSRP']

df1 = pd.read_csv("./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined_new.csv", usecols=columns)
df2 = pd.read_csv("./5Gdataset-master/Netflix/Static/Season3-StrangerThings/combined_new.csv", usecols= columns)


ax = df1.plot(x='Timestamp',y='DL_bitrate')
df2.plot(ax=ax,x='Timestamp',y='DL_bitrate')
plt.savefig('plot1.png')


#plot 2 Driving:  Netflix vs Amazon prime , DL_RATE VS Time 

df3 = pd.read_csv("./5Gdataset-master/Amazon_Prime/Driving/Season3-TheExpanse/combined_new.csv", usecols=columns)
df4 = pd.read_csv("./5Gdataset-master/Netflix/Driving/Season3-StrangerThings/combined_new.csv", usecols= columns)

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

plt.ylim(min(df1['RSRQ'].min(),df3['RSRQ'].min()),0)
ax = df1.plot(x='Timestamp',y='RSRQ')

df3.plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Static','Driving'])
plt.savefig('plot5.png')

#plot 6 Static vs Driving: NETFLIX,
# RSRQ VS Time

plt.ylim(min(df2['RSRQ'].min(),df4['RSRQ'].min()),0)

ax = df2.plot(x='Timestamp',y='RSRQ')

df4.plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Static','Driving'])
plt.savefig('plot6.png')

# #plot 7 Static vs Driving: Amazon prime,
# # RSRP VS Time

# plt.ylim(min(df1['RSRP'].min(),df3['RSRP'].min()), max(df1['RSRP'].max(),df3['RSRP'].max()))
# ax = df1.plot(x='Timestamp',y='RSRP')

# df3.plot(ax=ax,x='Timestamp',y='RSRP')
# plt.legend(['Static','Driving'])
# plt.savefig('plot7.png')


# #plot 8 Static vs Driving: NETFLIX,
# # RSRP VS Time

# plt.ylim(min(df2['RSRP'].min(),df4['RSRP'].min()), max(df2['RSRP'].max(),df4['RSRP'].max()))

# ax = df2.plot(x='Timestamp',y='RSRP')

# df4.plot(ax=ax,x='Timestamp',y='RSRP')
# plt.legend(['Static','Driving'])
# plt.savefig('plot8.png')
