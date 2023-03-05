import matplotlib.pyplot as plt
import pandas
import csv
import pandas as pd
import time
import numpy as np
import scipy as sp


'''
TO-DO : Follow the peak graph style
and number of rows : once combined_new is resolved 
'''

plt.rcParams["figure.figsize"] = [15.00, 5.00]
plt.rcParams["figure.autolayout"] = True

columns = ['Day','Timestamp','DL_bitrate','RSRQ','RSRP','RSSI']
df1 = pd.read_csv("./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv", usecols=columns)
df2 = pd.read_csv("./5Gdataset-master/Netflix/Static/Season3-StrangerThings/combined.csv", usecols= columns)

df3 = pd.read_csv("./5Gdataset-master/Amazon_Prime/Driving/Season3-TheExpanse/combined.csv", usecols=columns)
df4 = pd.read_csv("./5Gdataset-master/Netflix/Driving/Season3-StrangerThings/combined.csv", usecols= columns)

df5 = pd.read_csv("./5Gdataset-master/Netflix/Static/animated-RickandMorty/combined.csv", usecols= columns)
df6 = pd.read_csv("./5Gdataset-master/Netflix/Driving/animated-RickandMorty/combined.csv", usecols= columns)

# THINGS TO CHANGE :
# MOVING AVERAGE OR PEAK VALUE LINE GRAPH
# REDUCE X AXIS , RENAME X AXIS, labels


#plot 1 STATIC: Netflix vs Amazon prime , DL_RATE VS Time 

fig, axes = plt.subplots(nrows=2, ncols=2)

# Find minimum number of rows between df1 and df2
print(df1.loc[df1.Day=='Day1'].count()[0])
print(df2.loc[df2.Day=='Day1'].count()[0])
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df2.loc[df2.Day=='Day1'].count()[0])
print('df1 and df2\n',min_rows)

#df1.set_index('Timestamp', inplace = True)
ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,0])

'''USE FOR RUNNING AVERAGE'''
temp = df1.loc[df1.Day=='Day1'].head(min_rows).values.tolist()
print(type(temp))

#ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate')
df2.loc[df2.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 1')
plt.ylabel('DL_RATE')

#plt.savefig('plot1.png', dpi=640)


min_rows = min(df1.loc[df1.Day=='Day2'].count()[0],df2.loc[df2.Day=='Day2'].count()[0])
print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day2'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,1])
df2.loc[df2.Day=='Day2'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 2')
plt.ylabel('DL_RATE')

min_rows = min(df1.loc[df1.Day=='Day3'].count()[0],df2.loc[df2.Day=='Day3'].count()[0])
print('df1:',df1.loc[df1.Day=='Day4'].count()[0])
print('df2:',df2.loc[df2.Day=='Day4'].count()[0])
print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day3'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,0])
df2.loc[df2.Day=='Day3'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 3')
plt.ylabel('DL_RATE')

min_rows = min(df1.loc[df1.Day=='Day4'].count()[0],df2.loc[df2.Day=='Day4'].count()[0])
# print('df1:',df1.loc[df1.Day=='Day4'].count()[0])
# print('df2:',df2.loc[df2.Day=='Day4'].count()[0])
# print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day4'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,1])
df2.loc[df2.Day=='Day4'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 4')
plt.ylabel('DL_RATE')

axes[0,0].set(xlabel='DAY 1',ylabel='DL_RATE')
axes[0,1].set(xlabel='DAY 2',ylabel='DL_RATE')
axes[1,0].set(xlabel='DAY 3',ylabel='DL_RATE')
axes[1,1].set(xlabel='DAY 4',ylabel='DL_RATE')


plt.savefig('plot1.png', dpi=640)
plt.clf()
# --------------------------------------------------------------
# #plot 2 Driving:  Netflix vs Amazon prime , DL_RATE VS Time 

fig, axes = plt.subplots(nrows=2, ncols=2)


min_rows = min(df3.loc[df3.Day=='Day1'].count()[0],df4.loc[df4.Day=='Day1'].count()[0])
print('df3 and df4\n',min_rows)

#df1.set_index('Timestamp', inplace = True)
ax = df3.loc[df3.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,0])
df4.loc[df4.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 1')
plt.ylabel('DL_RATE')

min_rows = min(df3.loc[df3.Day=='Day2'].count()[0],df4.loc[df4.Day=='Day2'].count()[0])
print('df3 and df4\n',min_rows)

ax = df3.loc[df3.Day=='Day2'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,1])
df4.loc[df4.Day=='Day2'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 2')
plt.ylabel('DL_RATE')

min_rows = min(df3.loc[df3.Day=='Day3'].count()[0],df4.loc[df4.Day=='Day3'].count()[0])
print('df3 and df4\n',min_rows)

ax = df3.loc[df3.Day=='Day3'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,0])
df4.loc[df4.Day=='Day3'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 3')
plt.ylabel('DL_RATE')

min_rows = min(df3.loc[df3.Day=='Day4'].count()[0],df4.loc[df4.Day=='Day4'].count()[0])
print(print('df3 and df4\n',min_rows))

ax = df3.loc[df3.Day=='Day4'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,1])
df4.loc[df4.Day=='Day4'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 4')
plt.ylabel('DL_RATE')

axes[0,0].set(xlabel='DAY 1',ylabel='DL_RATE')
axes[0,1].set(xlabel='DAY 2',ylabel='DL_RATE')
axes[1,0].set(xlabel='DAY 3',ylabel='DL_RATE')
axes[1,1].set(xlabel='DAY 4',ylabel='DL_RATE')

plt.savefig('plot2.png', dpi=480)
plt.clf()

# --------------------------------------------------------------
#plot 3 Static vs Driving: Amazon prime,
# DL_RATE VS Time

fig, axes = plt.subplots(nrows=2, ncols=2)

# Find minimum number of rows between df1 and df2
print(df1.loc[df1.Day=='Day1'].count()[0])
print(df3.loc[df3.Day=='Day1'].count()[0])
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df3.loc[df3.Day=='Day1'].count()[0])

#df1.set_index('Timestamp', inplace = True)
ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,0])
#ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate')
df3.loc[df3.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 1')
plt.ylabel('DL_RATE')

#plt.savefig('plot1.png', dpi=640)


min_rows = min(df1.loc[df1.Day=='Day2'].count()[0],df3.loc[df3.Day=='Day2'].count()[0])
print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day2'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,1])
df3.loc[df3.Day=='Day2'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 2')
plt.ylabel('DL_RATE')

min_rows = min(df1.loc[df1.Day=='Day3'].count()[0],df3.loc[df3.Day=='Day3'].count()[0])
print('df1:',df1.loc[df1.Day=='Day4'].count()[0])
print('df2:',df3.loc[df3.Day=='Day4'].count()[0])
print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day3'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,0])
df3.loc[df3.Day=='Day3'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 3')
plt.ylabel('DL_RATE')

min_rows = min(df1.loc[df1.Day=='Day4'].count()[0],df3.loc[df3.Day=='Day4'].count()[0])
# print('df1:',df1.loc[df1.Day=='Day4'].count()[0])
# print('df2:',df2.loc[df2.Day=='Day4'].count()[0])
# print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day4'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,1])
df3.loc[df3.Day=='Day4'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 4')
plt.ylabel('DL_RATE')

axes[0,0].set(xlabel='DAY 1',ylabel='DL_RATE')
axes[0,1].set(xlabel='DAY 2',ylabel='DL_RATE')
axes[1,0].set(xlabel='DAY 3',ylabel='DL_RATE')
axes[1,1].set(xlabel='DAY 4',ylabel='DL_RATE')

plt.savefig('plot3.png', dpi=640)
plt.clf()

# #plot 4 Static vs Driving: NETFLIX,
# #DL_RATE VS Time

fig, axes = plt.subplots(nrows=2, ncols=2)


min_rows = min(df2.loc[df2.Day=='Day1'].count()[0],df4.loc[df4.Day=='Day1'].count()[0])
print('df3 and df4\n',min_rows)

#df1.set_index('Timestamp', inplace = True)
ax = df2.loc[df2.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,0])
df4.loc[df4.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 1')
plt.ylabel('DL_RATE')

min_rows = min(df2.loc[df2.Day=='Day2'].count()[0],df4.loc[df4.Day=='Day2'].count()[0])

ax = df2.loc[df2.Day=='Day2'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[0,1])
df4.loc[df4.Day=='Day2'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 2')
plt.ylabel('DL_RATE')

min_rows = min(df2.loc[df2.Day=='Day3'].count()[0],df4.loc[df4.Day=='Day3'].count()[0])

ax = df2.loc[df2.Day=='Day3'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,0])
df4.loc[df4.Day=='Day3'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 3')
plt.ylabel('DL_RATE')

min_rows = min(df2.loc[df2.Day=='Day4'].count()[0],df4.loc[df4.Day=='Day4'].count()[0])

ax = df2.loc[df2.Day=='Day4'].head(min_rows).plot(x='Timestamp',y='DL_bitrate',ax=axes[1,1])
df4.loc[df4.Day=='Day4'].head(min_rows).plot(ax=ax,x='Timestamp',y='DL_bitrate')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 4')
plt.ylabel('DL_RATE')

axes[0,0].set(xlabel='DAY 1',ylabel='DL_RATE')
axes[0,1].set(xlabel='DAY 2',ylabel='DL_RATE')
axes[1,0].set(xlabel='DAY 3',ylabel='DL_RATE')
axes[1,1].set(xlabel='DAY 4',ylabel='DL_RATE')

plt.savefig('plot4.png', dpi=480)
plt.clf()

# #plot 5 Static vs Driving: Amazon prime,
# # RSRQ VS Time

fig, axes = plt.subplots(nrows=2, ncols=2)

# Find minimum number of rows between df1 and df2
print(df1.loc[df1.Day=='Day1'].count()[0])
print(df3.loc[df3.Day=='Day1'].count()[0])
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df3.loc[df3.Day=='Day1'].count()[0])

#df1.set_index('Timestamp', inplace = True)
ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRQ',ax=axes[0,0])
#ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate')
df3.loc[df3.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')

plt.legend(['Static','Driving'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 1')
plt.ylabel('DL_RATE')

#plt.savefig('plot1.png', dpi=640)


min_rows = min(df1.loc[df1.Day=='Day2'].count()[0],df3.loc[df3.Day=='Day2'].count()[0])
print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day2'].head(min_rows).plot(x='Timestamp',y='RSRQ',ax=axes[0,1])
df3.loc[df3.Day=='Day2'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 2')
plt.ylabel('DL_RATE')

min_rows = min(df1.loc[df1.Day=='Day3'].count()[0],df3.loc[df3.Day=='Day3'].count()[0])
print('df1:',df1.loc[df1.Day=='Day4'].count()[0])
print('df2:',df3.loc[df3.Day=='Day4'].count()[0])
print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day3'].head(min_rows).plot(x='Timestamp',y='RSRQ',ax=axes[1,0])
df3.loc[df3.Day=='Day3'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 3')
plt.ylabel('DL_RATE')

min_rows = min(df1.loc[df1.Day=='Day4'].count()[0],df3.loc[df3.Day=='Day4'].count()[0])
# print('df1:',df1.loc[df1.Day=='Day4'].count()[0])
# print('df2:',df2.loc[df2.Day=='Day4'].count()[0])
# print('df1 and df2\n',min_rows)

ax = df1.loc[df1.Day=='Day4'].head(min_rows).plot(x='Timestamp',y='RSRQ',ax=axes[1,1])
df3.loc[df3.Day=='Day4'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')

plt.legend(['Amazon','Netflix'])
plt.title('STATIC: Netflix vs. Amazon Prime, DL_RATE', fontsize=8)
plt.xlabel('DAY 4')
plt.ylabel('DL_RATE')

axes[0,0].set(xlabel='DAY 1',ylabel='DL_RATE')
axes[0,1].set(xlabel='DAY 2',ylabel='DL_RATE')
axes[1,0].set(xlabel='DAY 3',ylabel='DL_RATE')
axes[1,1].set(xlabel='DAY 4',ylabel='DL_RATE')

plt.savefig('plot5.png', dpi=640)
plt.clf()

# #plot 6 Static vs Driving: NETFLIX,
# # RSRQ VS Time

# plt.ylim(-40,0)

# ax = df4.plot(x='Timestamp',y='RSRQ')

# df2.plot(ax=ax,x='Timestamp',y='RSRQ')
# plt.legend(['Static','Driving'])
# plt.savefig('plot6.png')

min_rows = min(df5.loc[df5.Day=='Day1'].count()[0],df6.loc[df6.Day=='Day1'].count()[0])

# from matplotlib.collections import LineCollection

# x = df5['Timestamp']
# y = df5.loc[df5.Day=='Day1'].head(min_rows)['RSRQ']
# cols = np.linspace(0,1,len(x))

# points = np.array([x, y]).T.reshape(-1, 1, 2)
# segments = np.concatenate([points[:-1], points[1:]], axis=1)

# fig, ax = plt.subplots()
# lc = LineCollection(segments, cmap='viridis')
# lc.set_array(cols)
# lc.set_linewidth(2)
# line = ax.add_collection(lc)
# fig.colorbar(line,ax=ax)

# print(points)
# print(segments)
#plt.show()

#ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot.scatter(x='Timestamp',y='RSRQ',c='RSRQ')
ax = df5.loc[df5.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRQ')
df6.loc[df6.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Static','Driving'])
plt.title('<RSRQ> NETFLIX: Static vs Driving')
plt.savefig('plot6.png')

# plot 7 Static: Netflix vs Amazon prime
# RSRQ vs Time
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df2.loc[df2.Day=='Day1'].count()[0])

ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRQ')
df2.loc[df2.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Amazon','Netflix'])
plt.title('<RSRQ> STATIC: Amazon vs Netflix')
plt.savefig('plot7.png')


# plot 8 Driving: Netflix vs Amazon prime
# RSRQ vs Time
min_rows = min(df3.loc[df3.Day=='Day1'].count()[0],df4.loc[df4.Day=='Day1'].count()[0])

ax = df3.loc[df3.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRQ')
df4.loc[df4.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRQ')
plt.legend(['Amazon','Netflix'])
plt.title('<RSRQ> DRIVING: Amazon vs Netflix')
plt.savefig('plot8.png')

# #plot 9 Static vs Driving: Amazon prime,
# # RSRP VS Time
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df3.loc[df3.Day=='Day1'].count()[0])

ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRP')
df3.loc[df3.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRP')
plt.legend(['Static','Driving'])
plt.title('<RSRP> AMAZON: Static vs Driving')
plt.savefig('plot9.png')

# #plot 10 Static vs Driving: NETFLIX,
# # RSRP VS Time
min_rows = min(df5.loc[df5.Day=='Day1'].count()[0],df6.loc[df6.Day=='Day1'].count()[0])

ax = df5.loc[df5.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRP')
df6.loc[df6.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRP')
plt.legend(['Static','Driving'])
plt.title('<RSRP> NETFLIX: Static vs Driving')
plt.savefig('plot10.png')

# plot 11 Static: Netflix vs Amazon prime
# RSRP vs Time
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df2.loc[df2.Day=='Day1'].count()[0])

ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRP')
df2.loc[df2.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRP')
plt.legend(['Amazon','Netflix'])
plt.title('<RSRP> STATIC: Amazon vs Netflix')
plt.savefig('plot11.png')


# plot 12 Driving: Netflix vs Amazon prime
# RSRP vs Time
min_rows = min(df3.loc[df3.Day=='Day1'].count()[0],df4.loc[df4.Day=='Day1'].count()[0])

ax = df3.loc[df3.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSRP')
df4.loc[df4.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSRP')
plt.legend(['Amazon','Netflix'])
plt.title('<RSRP> DRIVING: Amazon vs Netflix')
plt.savefig('plot12.png')



# #plot 13 Static vs Driving: Amazon prime,
# # RSSI VS Time
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df3.loc[df3.Day=='Day1'].count()[0])

ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSSI')
df3.loc[df3.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSSI')
plt.legend(['Static','Driving'])
plt.title('<RSSI> AMAZON: Static vs Driving')
plt.savefig('plot13.png')

# #plot 14 Static vs Driving: NETFLIX,
# # RSSI VS Time
min_rows = min(df5.loc[df5.Day=='Day1'].count()[0],df6.loc[df6.Day=='Day1'].count()[0])

ax = df5.loc[df5.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSSI')
df6.loc[df6.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSSI')
plt.legend(['Static','Driving'])
plt.title('<RSSI> NETFLIX: Static vs Driving')
plt.savefig('plot14.png')

# plot 15 Static: Netflix vs Amazon prime
# RSSI vs Time
min_rows = min(df1.loc[df1.Day=='Day1'].count()[0],df2.loc[df2.Day=='Day1'].count()[0])

ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSSI')
df2.loc[df2.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSSI')
plt.legend(['Amazon','Netflix'])
plt.title('<RSSI> STATIC: Amazon vs Netflix')
plt.savefig('plot15.png')


# plot 16 Driving: Netflix vs Amazon prime
# RSSI vs Time
min_rows = min(df3.loc[df3.Day=='Day1'].count()[0],df4.loc[df4.Day=='Day1'].count()[0])

ax = df3.loc[df3.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='RSSI')
df4.loc[df4.Day=='Day1'].head(min_rows).plot(ax=ax,x='Timestamp',y='RSSI')
plt.legend(['Amazon','Netflix'])
plt.title('<RSSI> DRIVING: Amazon vs Netflix')
plt.savefig('plot16.png')

