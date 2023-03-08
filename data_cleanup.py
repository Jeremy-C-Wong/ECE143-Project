import pandas as pd
import numpy as np
import glob
import os
import datetime as dt

def clean_files(basepath):
    '''
    Removes unnecessary columns and rows from each CSV file in the desired directory
    Changes time and date stamps to times
    '''
    # Obtain list of all CSV files in directory - assuming Python file is in same directory as master data folder (5Gdataset-master)
    files = glob.glob(basepath + '/**/*.csv', recursive=True)
    # Iterate through each file path in the master folder
    for file in files:

        df = pd.read_csv(file)

        # Try to add empty columns to use later and remove unnecessary columns (labels)
        try:    
            df.insert(0,'Day','')
            df.insert(0,'Date','')
            df['Rolling_avg'] = np.nan
            cleaned = df.drop(['Latitude','Longitude','Operatorname','CellID','PINGAVG','PINGMIN','PINGMAX','PINGSTDEV','PINGLOSS','CELLHEX','NODEHEX','LACHEX','RAWCELLID','NRxRSRP','NRxRSRQ'],axis=1)
        # Skip if attempting to clean already cleaned file
        except ValueError or KeyError:
            continue

        # Remove values when state is idle and when bitrate falls below threshold
        cleaned = cleaned[cleaned.State != 'I']
        cleaned = cleaned[cleaned.DL_bitrate > 10]
        # Split the Timestamp column into time and date columns
        cleaned[['Date','Timestamp']] = cleaned.Timestamp.str.split('_', expand=True)
        # Replace '-' with minimum values for RSSI and RSRQ
        cleaned['RSRQ'] = cleaned['RSRQ'].replace('-', -19.5)
        cleaned['RSSI'] = cleaned['RSSI'].replace('-', -110)
            
        # Create new file name by appending _cleaned before the .csv file extension
        new_name = file.removesuffix('.csv') + '_cleaned.csv'

        cleaned.to_csv(new_name)

def combine_files(basepath):
    '''
    This function is used to combine all the cleaned up .csv files into a single .csv file per folder
    '''
    # Get list of subdirectories in basepath
    workdir=os.listdir(basepath)
    if '.DS_Store' in workdir:
        workdir.remove('.DS_Store')

    files_combine=[]

    for dir_name in workdir:
        dir_path=os.path.join(basepath,dir_name)
        # Recursively iterate through subdirectories until it reaches a non-directory file
        if os.path.isdir(dir_path):
            combine_files(dir_path)
        else:
            if not dir_path.endswith('_cleaned.csv'):
                continue
            files_combine.append(dir_path)
    
    # If there is at least one data file in the subdirectory
    if(len(files_combine) > 0):
        # Create new dataframe with data from each file in the subdirectory
        df_concat = pd.concat([pd.read_csv(f) for f in files_combine], ignore_index=True)
        # Drop added index column if exists
        if('Unnamed: 0' in df_concat.columns):
            df_concat = df_concat.drop(['Unnamed: 0'], axis=1)
        # Write CSV file to new file called 'combined.csv' in current subdirectory
        df_concat.to_csv(os.path.join(os.path.dirname(dir_path), 'combined.csv'))

def set_day_nums(basepath):
    '''
    Fill in combined.csv files 'Day_Timeframe to prepare data for plotting
    '''
    files = glob.glob(basepath + '/**/*.csv', recursive=True)

    for file in files:

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
        # Set the Day_Timeframe column to the corresponding day numbers
        df['Day'] = np.select(day_conditions, day_numbers)

        # Re-order indices
        df.reset_index(drop=True, inplace=True)

        df.to_csv(file)

def convert_datetimes(basepath):
    '''
    Convert timestamps to datetime objects
    '''
    files = glob.glob(basepath + '/**/*.csv', recursive=True)

    for file in files:

        # Ignore all files except for combined.csv files
        if 'combined.csv' not in file:
            continue

        df = pd.read_csv(file)

        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%H.%M.%S').dt.time
        df.sort_values(by='Timestamp', inplace=True)

        df.to_csv(file)


basepath = './5Gdataset-master'

clean_files(basepath)
combine_files(basepath)
set_day_nums(basepath)
convert_datetimes(basepath)