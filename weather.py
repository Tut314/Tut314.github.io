import requests

# Vancouver
lat = 49.28
lon = -123.12

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]

temp = weather["temperature"]
wind = weather["windspeed"]

print("🌤 Current Weather in Vancouver:")
print(f"Temperature: {temp}°C")
print(f"Wind Speed: {wind} km/h")

print("\n🤖 Should you go outside?")

if temp < 5:
    print("❄️ Too cold. Stay inside and cry.")
elif wind > 20:
    print("🌪 Too windy. You might fly away.")
elif temp > 20:
    print("🌞 Perfect weather! Go touch some grass.")
else:
    print("🤔 Maybe... but bring a jacket.")