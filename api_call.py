import requests
import json
import datetime
import time
import clock
import times
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global variables that can be imported by other modules
converted_time = None
feel_temp = None
formatted_time = None
temp = None

def get_weather_data():
    """Fetch and process weather data from OpenWeatherMap API."""
    global converted_time, feel_temp, formatted_time, temp
    
    # Get configuration from environment
    api_key = os.getenv('WEATHER_API_KEY')
    lat = os.getenv('WEATHER_LAT')
    lon = os.getenv('WEATHER_LON')
    units = os.getenv('WEATHER_UNITS', 'imperial')
    
    if not all([api_key, lat, lon]):
        raise ValueError("Missing required environment variables. Check .env file.")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"
    
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    json_data = response.json()
    
    sunset = json_data['sys']['sunset']
    feel_temp = json_data['main']['feels_like']
    temp = json_data['main']['temp']
    
    converted_time = datetime.datetime.fromtimestamp(int(sunset))
    formatted_time = converted_time.strftime("%I:%M %p")
    
    return temp

if __name__ == "__main__":
    # This code only runs if api_call.py is run directly
    try:
        temp = get_weather_data()
        current_time = times.current_time()
        
        print()
        print(f"The time is {current_time}")
        print(f"It feels like {feel_temp:.1f}F outside.")
        print(f"But it is actually just {temp:.1f}F outside.")
        print(f"Today sunset was/will be at {formatted_time}")
        
        clock.stack_time(5, 20)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)