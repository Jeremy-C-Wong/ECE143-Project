import matplotlib.pyplot as plt
import pandas
import csv
import pandas as pd
import time
import numpy as np
import scipy as sp

def get_plot_labels(fpath1 : str, fpath2 : str):
    '''
    Determine labels for plot using filepath names
    Sample filepath: "./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv"
    '''

    p1_split = fpath1.split('/')
    p2_split = fpath2.split('/')

    strm_plat1, mode1, show1 = p1_split[2], p1_split[3], p1_split[4]
    strm_plat2, mode2, show2 = p2_split[2], p2_split[3], p2_split[4]

    strm_plat1 = strm_plat1.replace("_", " ")
    strm_plat2 = strm_plat2.replace("_", " ")

    # Determine title based on which two datasets are being compared
    if strm_plat1 == strm_plat2:
        legend = [mode1, mode2]
        title = '{sp}: {m1} vs. {m2}, '.format(sp=strm_plat1, m1=mode1, m2=mode2)
        fig_name = '{sp}_{m1}v{m2}_'.format(sp=strm_plat1[0], m1=mode1[0], m2=mode2[0])
    elif mode1 == mode2:
        legend = [strm_plat1, strm_plat2]
        title = '{mode}: {sp1} vs. {sp2}, '.format(mode=mode1, sp1=strm_plat1, sp2=strm_plat2)
        fig_name = '{mode}_{sp1}v{sp2}_'.format(mode=mode1[0], sp1=strm_plat1[0], sp2=strm_plat2[0])
    return legend, title, fig_name

def plot_df(fpath1 : str, fpath2 : str, y_axis='DL_bitrate', day='Day1', subplots=False, columns=['Day','Timestamp','DL_bitrate','RSRQ','RSRP','RSSI']
):
    '''
    Plot two dataframes with given settings
    '''

    plt.rcParams["figure.figsize"] = [15.00, 5.00]
    plt.rcParams["figure.autolayout"] = True

    df1 = pd.read_csv(fpath1, usecols=columns)
    df2 = pd.read_csv(fpath2, usecols=columns)

    legend, title, fig_name = get_plot_labels(fpath1, fpath2)

    # Find minimum number of rows between df1 and df2
    min_rows = min(df1.loc[df1.Day==day].count()[0],df2.loc[df2.Day==day].count()[0])

    if subplots:
        fig, axes = plt.subplots(nrows=2, ncols=2)

        for i in range(2):
            for j in range(2):
                ax = df1.loc[df1.Day==day].head(min_rows).plot(x='Timestamp',y=y_axis,ax=axes[i,j])
                #ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate')
                '''USE FOR RUNNING AVERAGE'''
                temp = df1.loc[df1.Day==day].head(min_rows).values.tolist()
                # print(type(temp))

                df2.loc[df2.Day==day].head(min_rows).plot(ax=ax,x='Timestamp',y=y_axis)
                plt.legend(legend)
                plt.title(title + y_axis, fontsize=8)
                plt.xlabel(day)
                plt.ylabel(y_axis)
                axes[i,j].set(xlabel=day.replace('Day', 'Day '),ylabel=y_axis,title=title)
                axes[i,j].legend(legend)

        plt.savefig('./plots/{fname}{y_name}_subplots.png'.format(fname=fig_name, y_name=y_axis))                   

    else:
        ax = df1.loc[df1.Day==day].head(min_rows).plot(x='Timestamp',y=y_axis)
        #ax = df1.loc[df1.Day=='Day1'].head(min_rows).plot(x='Timestamp',y='DL_bitrate')
        '''USE FOR RUNNING AVERAGE - type == list'''
        temp = df1.loc[df1.Day==day].head(min_rows).values.tolist()

        df2.loc[df2.Day==day].head(min_rows).plot(ax=ax,x='Timestamp',y=y_axis)
        plt.legend(legend)
        plt.title(title + y_axis, fontsize=8)
        plt.xlabel(day)
        plt.ylabel(y_axis)

        plt.savefig('./plots/{fname}{y_name}.png'.format(fname=fig_name, y_name=y_axis))                   


fpath1 = "./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv"
fpath2 = "./5Gdataset-master/Netflix/Static/Season3-StrangerThings/combined.csv"

fpath3 = "./5Gdataset-master/Amazon_Prime/Driving/Season3-TheExpanse/combined.csv"
fpath4 = "./5Gdataset-master/Netflix/Driving/Season3-StrangerThings/combined.csv"

fpath5 = "./5Gdataset-master/Netflix/Static/animated-RickandMorty/combined.csv"
fpath6 = "./5Gdataset-master/Netflix/Driving/animated-RickandMorty/combined.csv"

# DL_BITRATE
plot_df(fpath1, fpath2, subplots=True)  # Static: Amazon Prime vs. Netflix
plot_df(fpath3, fpath4, subplots=True)  # Driving: Amazon Prime vs. Netflix
plot_df(fpath1, fpath3)                 # Amazon Prime: Static vs. Driving
plot_df(fpath2, fpath4)                 # Netflix: Static vs. Driving

# RSRQ
plot_df(fpath1, fpath2, y_axis='RSRQ')
plot_df(fpath3, fpath4, y_axis='RSRQ')
plot_df(fpath1, fpath3, y_axis='RSRQ')
plot_df(fpath2, fpath4, y_axis='RSRQ')

# RSRP
plot_df(fpath1, fpath2, y_axis='RSRP')
plot_df(fpath3, fpath4, y_axis='RSRP')
plot_df(fpath1, fpath3, y_axis='RSRP')
plot_df(fpath2, fpath4, y_axis='RSRP')

# RSSI
plot_df(fpath1, fpath2, y_axis='RSSI')
plot_df(fpath3, fpath4, y_axis='RSSI')
plot_df(fpath1, fpath3, y_axis='RSSI')
plot_df(fpath2, fpath4, y_axis='RSSI')