**Group 18:** Shreyas Borse, I-Wei (Claire) Chen, Praharsha Mahurkar, Jeremy Wong

# Cellular Key Performance Indicators (KPIs) Analysis and Comparison

[Insert brief description of project]

**[TO-DO]**

Regarding GitHub Repository - Well documented, reusable Python module targeted at solving your proposal task. Follow all good coding practices and conventions discussed in class
* Include all your code as .py files (therefore remember to write modular code to make life easier) 
* Include 1 Jupyter notebook which shows all the visualizations you generated for your presentation.
* Include a readme file that explains your file structure, how to run your code, and name all third-party modules you are using.
* Include the final presentation as a pdf file

[Sample README Template](https://github.com/azavea/python-project-template/blob/master/README.md)

## File Structure

```
.
├── README.md               <- README
│
├── 5Gdataset-master
│   │
│   ├── Amazon_Prime        <- Data collected using Amazon Prime 
│   │   │        
│   │   ├── Driving         <- Data collected while driving
│   │   │   │
│   │   │   ├── animated-AdventureTime      <- Data collected from watching animated show
│   │   │   │   ├── B_2019.11.28_07.27.57_cleaned.csv
│   │   │   │   ├── B_2019.11.28_07.27.57.csv
│   │   │   │   ├── B_2019.11.28_10.14.25_cleaned.csv
│   │   │   │   ├── B_2019.11.28_10.14.25.csv
│   │   │   │   ├── ...
│   │   │   │   └── combined.csv            <- Cleaned and combined data from directory
│   │   │   │
│   │   │   └── Season3-TheExpanse      <- Data collected from watching filmed show
│   │   │       ├── B_2019.12.01_12.11.21_cleaned.csv
│   │   │       ├── B_2019.12.01_12.11.21.csv
│   │   │       ├── ...
│   │   │       └── combined.csv
│   │   │
│   │   └── Static          <- Data collected while stationary 
│   │       │                  (subdirectories follow same convention as Driving)
│   │       ├── animated-Ninjago
│   │       │   ├── B_2020.01.06_09.55.13_cleaned.csv
│   │       │   ├── B_2020.01.06_09.55.13.csv
│   │       │   ├── ...
│   │       │   └── combined.csv
│   │       │
│   │       └── Season3-TheExpanse
│   │           ├── ...
│   │           └── combined.csv
│   │
│   ├── Download            <- Data collected when downloading content
│   │   │
│   │   ├── Driving
│   │   │   └── ...
│   │   │
│   │   └── Static
│   │       └── ...
│   │
|   └── Netflix             <- Data collected using Netflix 
|       │                      (subdirectories follow same convention as Amazon Prime) 
│       ├── Driving
│       │   │
│       │   ├── animated-RickandMorty
│       │   │   └── ...
│       │   │
│       │   └── Season3-StrangerThings
│       │       └── ...
│       │
│       └── Static
│           │
│           ├── animated-RickandMorty
│           │   └── ...
│           │
│           └── Season3-StrangerThings
│               └── ...
│
├── plots                   <- Plots created by data_plot.py
│   │
│   ├── Amaz_SvD_DL_bitrate.png
│   ├── ...
│   └── Stat_AvN_RSSI.png
│
├── data_cleanup.py         <- Script to clean-up and consolidate data
│                              within each subdirectory of data folder
│
├── data_plot.py            <- Script to plot data from certain combined.csv files
│
├── generated_visualizations.ipynb          <- Jupyter notebook that creates  
│                                              visualizations for presentation
└── [insert PPTX file name here]            <- PPT of presentation


Additional template below

│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│
└── da-project         <- Source code for use in this project.
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
```

## How to Run

*Note: the output files (e.g. the cleaned data files and the plots) already exist in the repository, so the following steps are simply to describe the process as if they had not already been generated. If desired, you can remove the PNG files in the `plots` subdirectory, along with the `_cleaned.csv` and `combined.csv` files in each of the subdirectories of `5Gdataset-master`.*

First, navigate to the ECE143-Project directory.

Run `data_cleanup.py` to create cleaned and combined CSV files.

Following the previous step, there are two options for generating the plots:
1. Run `data_plot.py` to save all the plot figures into the `plots` subdirectory without showing the plots.
2. Run each cell in `generated_visualizations.ipynb` to show the plots in the output plots of each cell in the Jupyter Notebook (while also saving the plot figures into the aforementioned `plots` subdirectory).

If you wish to plot datasets or y-axis values not plotted in `data_plot.py` or `generated_visualizations.ipynb`, simply change or add the desired file paths at the top of these files and use as parameters to the `plot_df` function. Other parameters you can pass into `plot_df` are as follows:
* `y_axis (str)`: the column name to use for the y-axis of the plot(s); default is DL_bitrate
* `day (str)`: the day to use for the plot; default is 'Day1'; ignores this argument if `subplots == True`
* `subplots (boolean)`: plots only one plot if set to `False`, otherwise plots a 2x2 grid of subplots from Day 1 through Day 4 (assuming there are at least four days in the dataset); default is `False`
* `show (boolean)`: shows the figure if set to `False`, otherwise closes the figure; default is `False`
* `columns (list(str))`: the list of column names that will be accessed in the function call; default is `['Day','Timestamp','DL_bitrate','RSRQ','RSRP','RSSI']`

`[Insert code]`

## Third-Party Modules
* NumPy
* Pandas
