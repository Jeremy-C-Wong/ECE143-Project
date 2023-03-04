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

columns = ['Day','Timestamp','DL_bitrate','RSRQ','RSRP','RSSI']
df1 = pd.read_csv("./ECE143-Project-main/5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv", usecols=columns)
df2 = pd.read_csv("./ECE143-Project-main/5Gdataset-master/Netflix/Static/Season3-StrangerThings/combined.csv", usecols= columns)

df3 = pd.read_csv("./ECE143-Project-main/5Gdataset-master/Amazon_Prime/Driving/Season3-TheExpanse/combined.csv", usecols=columns)
df4 = pd.read_csv("./ECE143-Project-main/5Gdataset-master/Netflix/Driving/Season3-StrangerThings/combined.csv", usecols= columns)

df5 = pd.read_csv("./ECE143-Project-main/5Gdataset-master/Netflix/Driving/animated-RickandMorty/combined.csv", usecols= columns)
df6 = pd.read_csv("./ECE143-Project-main/5Gdataset-master/Netflix/Driving/animated-RickandMorty/combined.csv", usecols= columns)

# THINGS TO CHANGE :
# MOVING AVERAGE OR PEAK VALUE LINE GRAPH
# REDUCE X AXIS , RENAME X AXIS, labels


#plot 1 STATIC: Netflix vs Amazon prime , DL_RATE VS Time 

#df1.set_index('Timestamp', inplace = True)
ax = df1.loc[df1.Day=='Day1'].plot(x='Timestamp',y='DL_bitrate')
df2.loc[df2.Day=='Day1'].plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
#plt.savefig('plot1.png')


# #plot 2 Driving:  Netflix vs Amazon prime , DL_RATE VS Time 
ax = df3.loc[df1.Day=='Day1'].plot(x='Timestamp',y='DL_bitrate')
df4.loc[df4.Day=='Day1'].plot(ax=ax,x='Timestamp',y='DL_bitrate')
plt.legend(['Amazon','Netflix'])
# plt.savefig('plot2.png')
plt.show()

# #plot 3 Static vs Driving: Amazon prime,
# # DL_RATE VS Time

# ax = df1.plot(x='Timestamp',y='DL_bitrate')

# df3.plot(ax=ax,x='Timestamp',y='DL_bitrate')
# plt.legend(['Static','Driving'])
# plt.savefig('plot3.png')

# #plot 4 Static vs Driving: NETFLIX,
# #DL_RATE VS Time

# ax = df2.plot(x='Timestamp',y='DL_bitrate')

# df4.plot(ax=ax,x='Timestamp',y='DL_bitrate')
# plt.legend(['Static','Driving'])
# plt.savefig('plot4.png')

# #plot 5 Static vs Driving: Amazon prime,
# # RSRQ VS Time
# Indices3 = np.where(df3['RSRQ'] == '-')[0]
# Indices4 = np.where(df4['RSRQ'] == '-')[0]

# for i in Indices3:
#     df3 = df3.drop(i)

# for i in Indices4:
#     df4 = df4.drop(i)


# plt.ylim(-40,0)
# ax = df3.plot(x='Timestamp',y='RSRQ')

# df1.plot(ax=ax,x='Timestamp',y='RSRQ')
# plt.legend(['Static','Driving'])
# plt.savefig('plot5.png')

# #plot 6 Static vs Driving: NETFLIX,
# # RSRQ VS Time

# plt.ylim(-40,0)

# ax = df4.plot(x='Timestamp',y='RSRQ')

# df2.plot(ax=ax,x='Timestamp',y='RSRQ')
# plt.legend(['Static','Driving'])
# plt.savefig('plot6.png')



