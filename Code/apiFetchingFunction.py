import requests
import os
from os.path import dirname
import csv
import pandas as pd

def getWeatherData(year1, year2, your_api_key):
    # Get the response API to obtain historical data in Austin Texas for the given period
    response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=24&unitGroup=us&startDateTime={year1}-01-01T00:00:00&endDateTime={year2}-12-31T00:00:00&location=Austin,TX,US&key={your_api_key}&contentType=csv')

    # Check if the the status of the request is successful and proceed to obtaining data only if the request is successful 
    if response.status_code == 200:
        print("Your request has succeeded!")
        header = ["address","date time","minimum temperature","maximum temperature","temperature","dew point","relative humidity",
                  "heat index","wind speed","wind gust","wind direction","wind chill","precipitation","precipitation cover",
                  "snow depth","visibility","cloud cover","sea level pressure","weather type","latitude","longitude",
                  "resolved address","name","info","conditions"]
        
        # Use try/except to raise and catch ValueError whenever the response status code is 200 but it does not return request content
        try:
            # Create CSV reader instance to read the content of the obtained API respocset
            csv_reader = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')
            
            # Save the content of CSV reader into a list
            weather = [row for row in csv_reader]
            for i in range(len(weather[0])):
                weather[0][i] = weather[0][i].lower()
            if weather[0] != header:
                raise ValueError("Weather data cannot be obtained now, please check your API key or try later.")
                
            # Save the content of the list into a pandas DataFrame
            weather_df = pd.DataFrame(weather[1:], columns=weather[0])

            # Check if Data folder exists in the current working directory
            # If Data folder exists in the current working directory, save 'weather_14_15_df' into a csv file
            # If Data folder does not exist in the current working directory, create Data folder and save 'weather_14_15_df' into a csv file 
            curr_dir = os.getcwd()
            parent_folder = os.path.dirname(curr_dir) 
            if os.path.exists(parent_folder + "/Data"):
                folder = parent_folder + "/Data/"
                weather_df.to_csv(folder + f"Austin_TX_{year1}-01-01_to_{year2}-12-31.csv", index = False)
                print("Data is successfully saved.")
                pass
            else:
                os.mkdir(parent_folder + "/Data")
                folder = parent_folder + "/Data/"
                weather_df.to_csv(folder + f"Austin_TX_{year1}-01-01_to_{year2}-12-31.csv", index = False)
                print("Data is successfully saved.")
                pass
        except Exception as e:
            print(str(e))

    # If the request is unsuccessful print the following message
    else:
        print("Your request had failed, please try again.")
        pass
