import requests
import pandas as pd
import json

def get_nasa_weather(lat, lon, start_date, end_date):
    """
    Fetches Solar Irradiance and Temp from NASA POWER API.
    Dates must be in YYYYMMDD format.
    """
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "parameters": "ALLSKY_SFC_SW_DWN,T2M,RH2M,CLOUD_AMT", 
        "community": "RE", 
        "longitude": lon,
        "latitude": lat,
        "start": start_date,
        "end": end_date,
        "format": "JSON"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extracting the parameters into a DataFrame
    weather_dict = data['properties']['parameter']
    df_weather = pd.DataFrame(weather_dict)
    df_weather.index = pd.to_datetime(df_weather.index)
    df_weather.reset_index(inplace=True)
    df_weather.rename(columns={'index': 'Date', 
                               'ALLSKY_SFC_SW_DWN': 'Irradiance',
                               'T2M': 'Temp_2M'}, inplace=True)
    return df_weather

# Kapilvastu, Nepal Coordinates
LAT = 27.65
LON = 83.05

# Fetch data for 2081 BS period 
weather_df = get_nasa_weather(LAT, LON, "20240501", "20250430")
weather_df.to_csv('data/weather/kapilvastu_weather.csv', index=False)
print("Weather data saved successfully!")