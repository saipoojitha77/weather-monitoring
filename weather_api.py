# weather_api.py
import requests
from config import API_KEY

def get_weather_data(city):
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return None
