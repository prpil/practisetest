import requests
api_key = "8e0a94e302356894d6b9519c8e8a8510"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Toronto",
    "units": "metric",
    "appid": api_key
}
response = requests.get(url, params=params)
data = response.json()
if response.status_code == 200:
    print(f"Weather in {data['name']}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")
