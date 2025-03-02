import requests
import pandas as pd
import sqlalchemy
import time

# Configuration
API_KEY = "<insert you api key>"  # Weather API
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
LOCATIONS = ["Knoxville", "Chattanooga"]  # Cities to monitor
DB_URI = "postgresql+psycopg2://<insert your usrname>:<insert your pass>@localhost/weather_db"

# Connect to database
engine = sqlalchemy.create_engine(DB_URI)

def fetch_weather_data(city):
    """Fetch 5-day forecast weather data for a given city from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" #change between F or C
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}: {response.status_code} - {response.text}")
        return None

def transform_weather_data(data):
    """Extract multiple forecast entries from the API response and prepare them for database insertion."""
    records = []
    city_name = data["city"]["name"]
    
    for forecast in data["list"]:  # Iterate through all time intervals
        record = {
            "city": city_name,
            "datetime": pd.to_datetime(forecast["dt"], unit='s'),
            "temperature": forecast["main"]["temp"],
            "humidity": forecast["main"]["humidity"],
            "wind_speed": forecast["wind"]["speed"],
            "precip": forecast.get("rain", {}).get("3h", 0) + forecast.get("snow", {}).get("3h", 0),
            "cloud_cover": forecast["clouds"]["all"],
            "weather_condition": forecast["weather"][0]["description"]
        }
        records.append(record)
    
    return records

def load_data_to_db(weather_data):
    """Load transformed forecast data into the database."""
    df = pd.DataFrame(weather_data)
    df.to_sql("weather_forecast", engine, if_exists="append", index=False)

def etl_pipeline():
    """Full ETL process fetching and storing 5-day forecasts."""
    for city in LOCATIONS:
        data = fetch_weather_data(city)
        if data:
            transformed_data = transform_weather_data(data)
            load_data_to_db(transformed_data)
            print(f"Inserted forecast data for {city}")
        time.sleep(1)  # Avoid hitting API rate limits

if __name__ == "__main__":
    etl_pipeline()