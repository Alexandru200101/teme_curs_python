date = {
    "coord": {
        "lon": 26.1063,
        "lat": 44.4323
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 286.87,
        "feels_like": 286.07,
        "temp_min": 284.2,
        "temp_max": 289.74,
        "pressure": 1022,
        "humidity": 68
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.03,
        "deg": 260
    },
    "clouds": {
        "all": 0
    },
    "dt": 1666984646,
    "sys": {
        "type": 2,
        "id": 2037828,
        "country": "RO",
        "sunrise": 1666932421,
        "sunset": 1666969892
    },
    "timezone": 10800,
    "id": 683506,
    "name": "Bucharest",
    "cod": 200
}
# # Varianta 1 : extragem temperatura si descrierea vremii direct

# temp_kelvin = date["main"]["temp"]
# temp_celsius = temp_kelvin - 273.15

# # Extragem descrierea vremii (ex: "clear sky")
# descriere_cer = date["weather"][0]["description"]

# # Afișăm rezultatul
# print(f"În {date['name']} sunt {temp_celsius:.1f}°C și cerul este {descriere_cer}.")






# # Varianta 2 : extragem temperatura si descrierea vremii prin iterare

# # Extragem temperatura în Kelvin și o convertim în Celsius
# temp_kelvin = date["main"]["temp"]
# temp_celsius = temp_kelvin - 273.15

# # Afișăm temperatura
# print(f"În {date['name']} sunt {temp_celsius:.1f}°C.")

# # Iterăm prin toate condițiile meteo
# for conditie in date["weather"]:
    
#     descriere = conditie["description"]
#     print(f"Starea cerului: {descriere}")





# # Varianta 3 : returneaza un dictionar cu datele cerute
# rezultat = {
#     "oras": date["name"],
#     "temperatura_C": round(date["main"]["temp"] - 273.15, 2),
#     "descriere_cer": date["weather"][0]["description"]
# }

# print(rezultat)

def extrage_date_meteo(data):
    temp_kelvin = data.get("main", {}).get("temp", None)
    if temp_kelvin is None:
        temp_celsius = None
    else:
        temp_celsius = round(temp_kelvin - 273.15, 2)

    # Extragem descrierea cerului, dacă există
    descriere_cer = None
    weather_list = data.get("weather", [])
    if weather_list and isinstance(weather_list, list):
        descriere_cer = weather_list[0].get("description", None)

    oras = data.get("name", "Necunoscut")

    return {
        "oras": oras,
        "temperatura_C": temp_celsius,
        "descriere_cer": descriere_cer,
    }

rezultat = extrage_date_meteo(date)

print(f"În {rezultat['oras']} sunt {rezultat['temperatura_C']}°C și cerul este {rezultat['descriere_cer']}.")