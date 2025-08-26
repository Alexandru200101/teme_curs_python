# Conversii de temperatură
# Creează o clasă TemperatureConverter.
# Metode statice:
# celsius_to_fahrenheit(c)
# fahrenheit_to_celsius(f)
# Testează conversiile cu câteva valori.
import urllib.request
import urllib.error
import json
import sys
import matplotlib.pyplot as plt


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9


def get_weather_data(city, api_key):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}&contentType=json"
    try:
        with urllib.request.urlopen(url) as response:
            return json.load(response)
    except urllib.error.HTTPError as e:
        print('HTTP Error code:', e.code)
        sys.exit()
    except urllib.error.URLError as e:
        print('URL Error:', e.reason)
        sys.exit()

if __name__ == "__main__":
    API_KEY = "9QV4CQGTQHXEQZQDL66BFV9RG"  
    city = input("Introduceti orasul pentru prognoza meteo: ").strip()

    data = get_weather_data(city, API_KEY)

    
    days = data.get("days", [])
    dates = [day["datetime"] for day in days]
    temps_c = [day["temp"] for day in days]
    temps_f = [TemperatureConverter.celsius_to_fahrenheit(t) for t in temps_c]

    
    print(f"\nPrognoza temperaturii în {city}:")
    for date, c, f in zip(dates, temps_c, temps_f):
        print(f"{date}: {c}°C / {f:.1f}°F")


    plt.figure(figsize=(10,5))
    plt.plot(dates, temps_c, marker='o', color='blue', label="Celsius")
    plt.plot(dates, temps_f, marker='x', color='red', label="Fahrenheit")
    plt.title(f"Prognoza temperaturii în {city}")
    plt.xlabel("Zi")
    plt.ylabel("Temperatura")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

