import requests
import pandas as pd

# Define the location (latitude and longitude)
latitude = 12.922915

longitude = 80.127457


# Open-Meteo API URL for current weather data
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# Send GET request to Open-Meteo API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    current_weather = data.get('current_weather', {})
    
    # Extract relevant weather data
    weather_data = {
        'temperature': current_weather.get('temperature'),
        'windspeed': current_weather.get('windspeed'),
        'weather_code': current_weather.get('weathercode'),
        'latitude': latitude,
        'longitude': longitude
    }
    
    # Create DataFrame from the data
    df = pd.DataFrame([weather_data])
    
    # Print DataFrame
    print(df)
    
else:
    print("Failed to retrieve weather data", response.status_code)
from sqlalchemy import create_engine

# Create a SQLite engine
engine = create_engine('sqlite:///weather_data.db')

# Insert DataFrame into SQLite database (table name: 'weather')
df.to_sql('weather', con=engine, if_exists='append', index=False)
print("Weather data saved to database!")
