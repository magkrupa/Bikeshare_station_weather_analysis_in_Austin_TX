[![Open in Jupyter Notebook](https://img.shields.io/badge/Open%20in-Jupyter%20Notebook-orange?logo=jupyter)](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/HEAD?urlpath=lab)
![Python](https://img.shields.io/badge/Python-3.8-blue)


# Austin Bike-Sharing Project


## Understanding the Impact of Bike Stations on Cleaner Transportation

The Austin Bike-Sharing Project is designed to evaluate the role and effectiveness of bike stations in Austin in promoting cleaner and sustainable transportation methods. Our analysis extends beyond general usage of bike stations and delves into temporal patterns, including peak usage times and variations among different stations. We will explore various factors such as popular commuter routes, bookings per station, trip durations, station activity, peak and off-peak usage, among others. Through this, we aim to provide comprehensive insights into the efficiency of Austin's bike-sharing infrastructure. Moreover, we hope to identify potential areas that could benefit from the implementation or enhancement of bike stations.

Throughout the project, we will perform rigorous data cleaning, exploratory data analysis, in-depth analysis, and data transformation. These steps will enable us to conduct detailed feature engineering for a deeper analysis of the collected data.


## Data Sources

    - Bike Trip data: This dataset includes information on bike trips taken from December 2013 to March 2023. 
    - Bike Station data: This dataset provides information on all active and inactive bike stations in Austin. 
    - Weather Data Base - Visual Crossing (https://www.visualcrossing.com/). This dataset includes information 
      on weather conditions taken from 01.01.2014 to 31.12.2022 To obtain the historical data on weather conditions
      we used API fetching. If you are interested in code, have a look at `api_fetching.ipynb` and `apiFetchingFunction.py`files.


## Instructions

For the best experience and accurate results, it's essential to execute the code cells in the provided Jupyter notebook in the order they appear. As you work through this project, you may encounter the need to install additional Python libraries, such as Folium and Geopy, which are not included in the standard Python distribution.

To install these libraries, you can use the pip package manager, which is typically included with your Python installation. For instance, to install Folium, you would use the following command in your command line interface: *pip install folium* 

Please ensure these libraries are correctly installed before attempting to run the code cells that depend on them. This will ensure the smooth running of the program and the accuracy of the results.

```
Project
├─ Code                             <- The code used for the analysis 
│  ├─ data_prep.ipynb              <- reads in, cleans and prepares data for analysis, also includes plots
│  ├─ analysis.ipynb                <- contains analysis and results
│  ├─ api_fetching.ipynb            <- imports historical data on weather conditions in Austin, Texas from 2014 to 2022
│  ├─ apiFetchingFunction           <- function to get historical data through API fetching
│  └─ standartiseSubscriptions.py   <- function to standartise subscription names
│    
│   
├─ Data                             <- all the datasets used for this project can be found in the latest releases
├─ Figures                          <- all figures  in PNG or PDF format
├─ Licence
├─ README.md
└─ Requirements.txt                 <- contains all the required libraries
```
<!-- ©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator) -->

-------------------------------------------------------------------------------
Thank you for using this code. We hope you find it both useful and enjoyable to use. \
Please don't hesitate to reach out if you require any further assistance.

-------------------------------------------------------------------------------

### Credits: 
-[Dinara Akmurzina](https://github.com/dakmurzina), \
-[Magdalena Krupa](https://github.com/magkrupa), \
-[Marina Zviagina](https://github.com/marina-zviagina), \
-[Sharyn McPherson](https://github.com/ShaMcP), \
-[Vanessa Chan](https://github.com/vjfychan), \
-[Lamiaa Bahgat](https://github.com/LamiaaBahgat).