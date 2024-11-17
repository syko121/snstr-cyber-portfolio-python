import requests

def get_weather(city):
    """Fetch weather for a specific city using wttr.in."""
    try:
        print(f"\nFecthing weather information for {city}...\n")
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to get weather data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f" An error has occured: {e}")
