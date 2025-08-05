import requests

def fetch_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url)
        data = response.json()

        current = data['current_condition'][0]
        print(f"\n Weather in {city.title()}")
        print(f"Temperature: {current['temp_C']}°C")
        print(f"Feels Like: {current['FeelsLikeC']}°C")
        print(f"Humidity: {current['humidity']}%")
        print(f"Condition: {current['weatherDesc'][0]['value']}")
    
    except Exception as e:
        print("Failed to fetch weather data:", e)

fetch_weather("Raipur")
fetch_weather("Durg")
