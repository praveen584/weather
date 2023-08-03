import requests
from datetime import datetime

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_weather_by_date(weather_data, date):
    for item in weather_data["list"]:
        if date in item["dt_txt"]:
            return item["main"]["temp"]
    return None

def get_wind_speed_by_date(weather_data, date):
    for item in weather_data["list"]:
        if date in item["dt_txt"]:
            return item["wind"]["speed"]
    return None

def get_pressure_by_date(weather_data, date):
    for item in weather_data["list"]:
        if date in item["dt_txt"]:
            return item["main"]["pressure"]
    return None

def main():
   weather_data = get_weather_data()
    if not weather_data:
        return

    print("Available dates in weather data:")
    for item in weather_data["list"]:
        print(item["dt_txt"])

    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Terminating the program.")
            break
        elif choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

            temperature = get_weather_by_date(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Weather data not found for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print("Weather data not found for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

            pressure = get_pressure_by_date(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Weather data not found for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
