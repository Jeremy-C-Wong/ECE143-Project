import pandas as pd
import glob
import os

using_windows = True    # controls file access - change to False if not using Windows system

if using_windows:
    basepath = '.\\5Gdataset-master'
else:
    basepath = './5Gdataset-master'

def clean_ind_files():
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

        # Try to remove unnecessary columns (labels)
        try:    
            cleaned = df.drop(['Latitude','Longitude','Operatorname','CellID','PINGAVG','PINGMIN','PINGMAX','PINGSTDEV','PINGLOSS','CELLHEX','NODEHEX','LACHEX','RAWCELLID','NRxRSRP','NRxRSRQ'],axis=1)
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
        df_concat.to_csv(os.path.join(os.path.dirname(dir_path),'combined_new.csv'))

clean_ind_files()
dir_path_under(basepath)
