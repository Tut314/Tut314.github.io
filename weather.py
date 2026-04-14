import requests

# Vancouver
lat = 49.28
lon = -123.12

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]

print("Current Weather in Vancouver:")
print(f"Temperature: {weather['temperature']}°C")
print(f"Wind Speed: {weather['windspeed']} km/h")