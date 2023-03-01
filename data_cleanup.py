import pandas as pd
import numpy as np
import glob
import os

using_windows = True    # controls file access - change to False if not using Windows system

if using_windows:
    basepath = '.\\5Gdataset-master'
else:
    basepath = './5Gdataset-master'

def clean_files(basepath):
    '''
    Removes unnecessary columns and rows from each CSV file in the desired directory
    Changes time and date stamps to times
    '''
    # Obtain list of all CSV files in directory - assuming Python file is in same directory as master data folder (5Gdataset-master)
    if (using_windows): # for Windows users
        files = glob.glob(basepath + '\\**\\*.csv', recursive=True)     
    else: # for non-Windows users
        files = glob.glob(basepath + '/**/*.csv', recursive=True)
        print(files)
    # Iterate through each file path in the master folder
    for file in files:

        # Change file path to access on Windows
        if (using_windows):
            file = file.replace('\\','\\\\')
        else:
            file = file.replace('\\','/')

        # Create DataFrame
        df = pd.read_csv(file)

        # Try to add empty 'Date' column and remove unnecessary columns (labels)
        try:    
            df.insert(1,'Timeframe','')
            df.insert(0,'Date','')
            df.insert(1,'Day#_Timeframe','')
            cleaned = df.drop(['Latitude','Longitude','Operatorname','CellID','PINGAVG','PINGMIN','PINGMAX','PINGSTDEV','PINGLOSS','CELLHEX','NODEHEX','LACHEX','RAWCELLID','NRxRSRP','NRxRSRQ'],axis=1)
        # Skip if attempting to clean already cleaned file
        except ValueError or KeyError:
            continue

        # Iterate through each index of the DateFrame
        for x in cleaned.index:
            # Get date (YYYY.MM.DD) and time (HH.MM.SS) from Timestamp label
            timestamp_date = cleaned.loc[x,'Timestamp'].split('_')[0]
            timestamp_time = cleaned.loc[x,'Timestamp'].split('_')[1]
            # Set date column to date and timestamps to only time (remove the date)
            cleaned.loc[x,'Date'] = timestamp_date
            cleaned.loc[x,'Timestamp'] = timestamp_time  
            # Remove any rows with State 'I' (idle state)   
            if cleaned.loc[x,'State'] == 'I':
                cleaned.drop(x,inplace=True)
                continue
            if cleaned.loc[x,'DL_bitrate'] <= 10:
                cleaned.drop(x,inplace=True)
                continue
            

        # Create new file name by appending _cleaned before the .csv file extension
        new_name = file.removesuffix('.csv')
        new_name += '_cleaned.csv'

        # Write DataFrame to a new file or overwrite existing file
        cleaned.to_csv(new_name)

def dir_path_under(basepath):
    '''
    This function is used to combine all the cleaned up .csv files into a single .csv file per folder
    '''
    workdir=os.listdir(basepath)
    if '.DS_Store' in workdir:
        workdir.remove('.DS_Store')
    files_combine=[]
    for dir_name in workdir:
        dir_path=os.path.join(basepath,dir_name)
        if os.path.isdir(dir_path):
            dir_path_under(dir_path)
        else:
            if not dir_path.endswith('_cleaned.csv'):
                continue
            files_combine.append(dir_path)
    
    if(len(files_combine)>0):
        df_concat=pd.concat([pd.read_csv(f) for f in files_combine],ignore_index=True)
        if('Unnamed: 0' in df_concat.columns):
            df_concat=df_concat.drop(['Unnamed: 0'],axis=1)
        df_concat.to_csv(os.path.join(os.path.dirname(dir_path),'combined.csv'))

def get_time_range(hms):
    '''
    Return 3-hour timeframe that a given hour falls under
    '''
    hour = int(hms.split('.')[0])

    timeframe = ''
    # Create list of conditions to determine the time frame
    conditions = [(6 <= hour < 9),(9 <= hour < 12),(12 <= hour < 15),(15 <= hour < 18),(18 <= hour < 21)]
    # Create list of timeframes
    choices = ['0600-0859','0900-1159','1200-1459','1500-1759','1800-2059']
    # Determine timeframe based on hour value
    timeframe = str(np.select(conditions,choices))

    return timeframe

def set_day_nums(basepath):
    '''
    Fill in combined.csv files 'Day#_Timeframe to prepare data for plotting
    '''
    if (using_windows):
        files = glob.glob(basepath + '\\**\\*.csv', recursive=True)     
    else:
        files = glob.glob(basepath + '/**/*.csv', recursive=True)
        print(files)
    for file in files:
        if (using_windows):
            file = file.replace('\\','\\\\')
        else:
            file = file.replace('\\','/')

        # Ignore all files except for combined.csv files
        if 'combined.csv' not in file:
            continue

        df = pd.read_csv(file)

        # Remove extra index column
        if('Unnamed: 0' in df.columns):
            df = df.drop(['Unnamed: 0'],axis=1)
        # Create list of unique dates in dataframe
        date_list = df['Date'].unique()
        # Sort date list in chronological order
        date_list.sort()

        # Create list of conditions for the Date column to determine test day number (e.g. Day1, Day2, ...)
        day_conditions = [(df['Date'] == date_list[i]) for i in range(len(date_list))]
        # Create list of day numbers
        day_numbers = ['Day' + str(i+1) for i in range(len(date_list))]
        # Set the Day#_Timeframe column to the corresponding day numbers
        df['Day#_Timeframe'] = np.select(day_conditions, day_numbers)
        # Set the Timeframe column to the corresponding timeframes
        df['Timeframe'] = df['Timestamp'].apply(get_time_range)
        # Append the timeframes to the Day#_Timeframe column
        df['Day#_Timeframe'] = df['Day#_Timeframe'] + '_' + df['Timeframe']

        # FOR TESTING: determine how many Day#_Timeframe periods are in the files to plot
        dayn_tf_list = df['Day#_Timeframe'].unique()
        if 'Season3' in file:
            print(file)
            print(dayn_tf_list)
            print('length:',len(dayn_tf_list))

        df.to_csv(file)

        

#clean_files(basepath)
#dir_path_under(basepath)
set_day_nums(basepath)