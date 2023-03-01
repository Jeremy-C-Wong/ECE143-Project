**Group 18:** Shreyas Borse, I-Wei (Claire) Chen, Praharsha Mahurkar, Jeremy Wong

# Cellular Key Performance Indicators (KPIs) Analysis and Comparison

**[TO-DO]**

Regarding GitHub Repository - Well documented, reusable Python module targeted at solving your proposal task. Follow all good coding practices and conventions discussed in class
* Include all your code as .py files (therefore remember to write modular code to make life easier) 
* Include 1 Jupyter notebook which shows all the visualizations you generated for your presentation.
* Include a readme file that explains your file structure, how to run your code, and name all third-party modules you are using. 
* Include the final presentation as a pdf file

## File Structure

```
.
├── README.md               <- README
├── 5Gdataset-master
│   ├── Amazon_Prime        <- Data collected using Amazon Prime         
│   │   ├── Driving         <- Data collected while driving
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
│   │   ├── Driving
│   │   │   └── ...
│   │   │
│   │   └── Static
│   │       └── ...
│   │
|   └── Netflix             <- Data collected using Netflix 
|       │                      (subdirectories follow same convention as Amazon Prime) 
│       ├── Driving
│       │   ├── animated-RickandMorty
│       │   │   └── ...
│       │   └── Season3-StrangerThings
│       │       └── ...
│       │
│       └── Static
│           ├── animated-RickandMorty
│           │   └── ...
│           └── Season3-StrangerThings
│               └── ...
│
├── data_cleanup.py         <- Script to clean-up and consolidate data
│                              within each subdirectory of data folder
│
├── data_plot.py            <- Script to plot data from certain combined.csv files
│
├── generated_visualizations.ipynb          <- Jupyter notebook containing visualizations 
│                                              generated for presentation


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

## How to Use

## Third-Party Modules
* NumPy
* Pandas
