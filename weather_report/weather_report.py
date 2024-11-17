from weather_report.weather_module import get_weather

def weather_report():
    """Prompts the user for a city and displays the weather."""
    city = input("Enter a city to get its weather: ")
    get_weather(city)

if __name__ == "__main__":
    weather_report()
