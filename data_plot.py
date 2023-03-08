import matplotlib.pyplot as plt
import pandas as pd

def get_plot_labels(fpath1 : str, fpath2 : str, subplots : bool):
    '''
    Determine labels for plot using filepath names
    Sample filepath: "./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv"
    Parameters:
        fpath1 (str): file path of 1st dataframe
        fpath2 (str): file path of 2nd dataframe
        subplots (bool): used to determine whether or not to include rolling averages in legend
        comparison (str): the factors being compared
    '''

    p1_split = fpath1.split('/')
    p2_split = fpath2.split('/')

    # Get streaming platform and mobility status from each dataframe
    strm_plat1, mode1 = p1_split[2], p1_split[3]
    strm_plat2, mode2 = p2_split[2], p2_split[3]

    strm_plat1 = strm_plat1.replace("_", " ")
    strm_plat2 = strm_plat2.replace("_", " ")

    # Determine legend, title, and file name based on which two datasets are being compared
    if strm_plat1 == strm_plat2:    # if the streaming platforms are the same
        if subplots: legend = [mode1, mode2]
        else: legend = [mode1, mode2, mode1+' Rolling Avg.', mode2+' Rolling Avg.']
        title = '{sp}: {m1} vs. {m2}, '.format(sp=strm_plat1, m1=mode1, m2=mode2)
        fig_name = '{sp}_{m1}v{m2}_'.format(sp=strm_plat1[0:4], m1=mode1[0], m2=mode2[0])
        comparison = 'mobility pattern'
    elif mode1 == mode2:            # if the mobility statuses are the same
        if subplots: legend = [strm_plat1, strm_plat2]
        else: legend = [strm_plat1, strm_plat2, strm_plat1+' Rolling Avg.', strm_plat2+' Rolling Avg.']
        title = '{mode}: {sp1} vs. {sp2}, '.format(mode=mode1, sp1=strm_plat1, sp2=strm_plat2)
        fig_name = '{mode}_{sp1}v{sp2}_'.format(mode=mode1[0:4], sp1=strm_plat1[0], sp2=strm_plat2[0])
        comparison = 'streaming platform'
    return legend, title, fig_name, comparison

def plot_df(fpath1 : str, fpath2 : str, y_axis='DL_bitrate', day='Day1', subplots=False, show=False, columns=['Day','Timestamp','DL_bitrate','RSRQ','RSRP','RSSI']
):
    '''
    Plot two dataframes with given settings
    Parameters:
        fpath1 (str): file path of 1st dataframe
        fpath2 (str): file path of 2nd dataframe
        y_axis (str): column to use as y-axis of plots
        day (str): Day number to use
        subplots (bool): False if plotting single plot, True if plotting 2x2 grid of plots
        show (bool): True if showing plot, False otherwise
        columns (list(str)): names of columns to use in plots
    '''

    assert isinstance(fpath1, str) and isinstance(fpath2, str)
    assert '.csv' in fpath1 and '.csv' in fpath2
    assert 'Day' in columns and 'Timestamp' in columns and y_axis in columns

    df1 = pd.read_csv(fpath1, usecols=columns)
    df2 = pd.read_csv(fpath2, usecols=columns)
    assert y_axis in df1.columns and y_axis in df2.columns
    assert day in df1.Day.values and day in df2.Day.values

    plt.rcParams["figure.figsize"] = [25.00, 10.00]
    plt.rcParams["figure.autolayout"] = True

    legend, title, fig_name, comparison = get_plot_labels(fpath1, fpath2, subplots)
    # Create dictionary for units corresponding to each value and assign value and unit to y_label
    units = {'DL_bitrate': 'kbps', 'RSRQ': 'dB', 'RSRP': 'dBm', 'RSSI': 'dBm'}
    y_label = '{y} ({u})'.format(y=y_axis, u=units[y_axis])

    if subplots:
        # Set up 2x2 grid of subplots
        fig, axes = plt.subplots(nrows=2, ncols=2)
        # x-axis coordinate for displaying text in terms of Axes coordinates (x: [0,1])
        x_dist = 0.855
        if comparison == 'mobility pattern': x_dist = 0.90
        # Iterate through each row and column of grid
        for i in range(2):
            for j in range(2):
                # Set day number based on row and column number
                day = '{d}{n}'.format(d=day[:-1], n=2*i+j+1)
                # Find minimum number of rows between df1 and df2
                min_rows = min(df1.loc[df1.Day==day].count()[0], df2.loc[df2.Day==day].count()[0])
                # Plot values from datasets
                ax = df1.loc[df1.Day==day].head(min_rows).plot(x='Timestamp', y=y_axis, ax=axes[i,j])
                df2.loc[df2.Day==day].head(min_rows).plot(ax=ax, x='Timestamp', y=y_axis)
                # Calculate and display averages of the y-values for each dataset over the given time period
                avg_str1 = 'Avg. {l0}: {val} {u}'.format(l0=legend[0].split(' ')[0], val=round(df1.loc[df1.Day==day][y_axis].mean(), 2), u=units[y_axis])
                avg_str2 = 'Avg. {l1}: {val} {u}'.format(l1=legend[1], val=round(df2.loc[df2.Day==day][y_axis].mean(), 2), u=units[y_axis])
                ax.text(x_dist, 0.94, avg_str1, fontsize=10, color='steelblue', weight='bold', horizontalalignment='right', transform=ax.transAxes)
                ax.text(x_dist, 0.89, avg_str2, fontsize=10, color='darkorange', weight='bold', horizontalalignment='right', transform=ax.transAxes)
                # Set subplot axis labels, title, and legend
                axes[i,j].set(xlabel=day.replace('Day', 'Day '), ylabel=y_label, title=title+y_axis)
                axes[i,j].legend(legend, loc='upper right')

        # Saves into plots subdirectory in format <constant value>_<comparison_values>_<y_value>.png
        # e.g. Amaz_SvD_RSRP.png where it compares RSRP values of Static and Driving for Amazon Prime
        plt.savefig('./plots/{fname}{y_name}_subplots.png'.format(fname=fig_name, y_name=y_axis), dpi=860)
        if show: plt.show()
        else: plt.close()

    else:
        x_dist = 0.895
        if comparison == 'mobility pattern': x_dist = 0.915
        min_rows = min(df1.loc[df1.Day==day].count()[0], df2.loc[df2.Day==day].count()[0])
        # Adding rolling average column to the dataframes
        mask1 = df1.Day==day
        mask2 = df2.Day==day
        df1.loc[mask1, 'Rolling_avg'] = df1.loc[mask1, y_axis].rolling(20).mean()
        df2.loc[mask2, 'Rolling_avg'] = df2.loc[mask2, y_axis].rolling(20).mean()
        # Plot values and rolling averages of both datasets
        ax = df1.loc[df1.Day==day].head(min_rows).plot(x='Timestamp', y=y_axis, linewidth=1)
        df2.loc[df2.Day==day].head(min_rows).plot(ax=ax, x='Timestamp', y=y_axis, linewidth=1)
        df1.loc[df1.Day==day].head(min_rows).plot(ax=ax, x='Timestamp', y='Rolling_avg', linewidth=2.5)
        df2.loc[df2.Day==day].head(min_rows).plot(ax=ax, x='Timestamp', y='Rolling_avg', linewidth=2.5)
        # Calculate and display averages of the y-values for each dataset over the given time period
        avg_str1 = 'Avg. {l0}: {val} {u}'.format(l0=legend[0].split(' ')[0], val=round(df1.loc[df1.Day==day][y_axis].mean(), 2), u=units[y_axis])
        avg_str2 = 'Avg. {l1}: {val} {u}'.format(l1=legend[1], val=round(df2.loc[df2.Day==day][y_axis].mean(), 2), u=units[y_axis])
        ax.text(x_dist, 0.97, avg_str1, fontsize=10, color='steelblue', weight='bold', horizontalalignment='right', transform=ax.transAxes)
        ax.text(x_dist, 0.95, avg_str2, fontsize=10, color='darkorange', weight='bold', horizontalalignment='right', transform=ax.transAxes)
        # Set plot labels, title, legend
        ax.set(xlabel=day, ylabel=y_label, title=title+y_axis)
        plt.legend(legend, loc='upper right')

        plt.savefig('./plots/{fname}{y_name}.png'.format(fname=fig_name, y_name=y_axis), dpi=860)
        if show: plt.show()
        else: plt.close()


fpath1 = "./5Gdataset-master/Amazon_Prime/Static/Season3-TheExpanse/combined.csv"
fpath2 = "./5Gdataset-master/Netflix/Static/Season3-StrangerThings/combined.csv"

fpath3 = "./5Gdataset-master/Amazon_Prime/Driving/Season3-TheExpanse/combined.csv"
fpath4 = "./5Gdataset-master/Netflix/Driving/Season3-StrangerThings/combined.csv"

fpath5 = "./5Gdataset-master/Netflix/Static/animated-RickandMorty/combined.csv"
fpath6 = "./5Gdataset-master/Netflix/Driving/animated-RickandMorty/combined.csv"

# DL_BITRATE
plot_df(fpath1, fpath2, subplots=True)  # Static: Amazon Prime vs. Netflix
plot_df(fpath3, fpath4, subplots=True)  # Driving: Amazon Prime vs. Netflix
plot_df(fpath1, fpath3, subplots=True)  # Amazon Prime: Static vs. Driving
plot_df(fpath2, fpath4, subplots=True)  # Netflix: Static vs. Driving

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