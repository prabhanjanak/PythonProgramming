import json

with open('weather_data.json') as f:
    data = json.load(f)

current_temp, humidity, weather_desc = data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']

print(f"Current temperature: {current_temp}°C\nHumidity: {humidity}%\nWeather description: {weather_desc}")
