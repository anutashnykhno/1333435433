import requests
from datetime import datetime

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "cnt": 7
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        for forecast in data['list']:
            timestamp = forecast['dt']
            date = datetime.fromtimestamp(timestamp)
            temperature = forecast['main']['temp']
            day_of_week = date.strftime("%A")

            print(f"{day_of_week}: {temperature}°C")
    else:
        print("Не вдалося отримати дані про погоду.")


api_key = "YOUR_API_KEY"
city_name = "Назва вашого міста"

get_weather(api_key, city_name)

