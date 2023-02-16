import pandas as pd
import glob

using_windows = True    # controls file access - change to False if not using Windows system

# Obtain list of all CSV files in directory - assuming Python file is in same directory as master data folder (5Gdataset-master)
if (using_windows): # for Windows users
    files = glob.glob('.\\5Gdataset-master\\**\\*.csv', recursive=True)     
else: # for non-Windows users
    files = glob.glob('./5Gdataset-master/**/*.csv', recursive=True)

# Iterate through each file path in the master folder
for file in files:
    # Change file path to access on Windows
    if (using_windows):
        file = file.replace('\\','\\\\')
    else:
        file = file.replace('\\','/')

    # Create DataFrame
    df = pd.read_csv(file)

    # Try to remove unnecessary columns (labels)
    try:    
        cleaned = df.drop(['Operatorname','CellID','PINGAVG','PINGMIN','PINGMAX','PINGSTDEV','PINGLOSS','CELLHEX','NODEHEX','LACHEX','RAWCELLID','NRxRSRP','NRxRSRQ'],axis=1)
    # Skip if attempting to clean already cleaned file
    except KeyError:    
        continue

    # Iterate through each index of the DateFrame
    for x in cleaned.index:
        # Get time (HH.MM.SS) from Timestamp label
        timestamp_time = cleaned.loc[x,'Timestamp'].split('_')[1]
        # Set timestamps to only time (remove the date)
        cleaned.loc[x,'Timestamp'] = timestamp_time  
        # Remove any rows with State 'I' (idle state)   
        if cleaned.loc[x,'State'] == 'I':
            cleaned.drop(x,inplace=True)

    # Create new file name by appending _cleaned before the .csv file extension
    new_name = file.removesuffix('.csv')
    new_name += '_cleaned.csv'

    # Write DataFrame to a new file or overwrite existing file
    cleaned.to_csv(new_name)
