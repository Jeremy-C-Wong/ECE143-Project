import pandas as pd
import glob
import os

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

                


basepath='./5Gdataset-master'
dir_path_under(basepath)


