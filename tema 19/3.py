import requests


# url = "https://wttr.in/?format=j1"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
    
#     for zi in data["weather"]:
#         date = zi["date"]
#         max_temp = zi["maxtempC"]
#         min_temp = zi["mintempC"]
#         descriere = zi["hourly"][0]["weatherDesc"][0]["value"]  # prima descriere din zi
        
#         print(f"📅 {date}: {min_temp}°C - {max_temp}°C, {descriere}")
# else:
#     print("Eroare:", response.status_code)

def f(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Eroare: {response.status_code}"
    
url = "https://wttr.in/?format=j1"
data = f(url)
for zi in data["weather"]:
    date = zi["date"]
    max_temp = zi["maxtempC"]
    min_temp = zi["mintempC"]
    descriere = zi["hourly"][0]["weatherDesc"][0]["value"]   
    print(f" {date}: {min_temp}°C - {max_temp}°C, {descriere}")
    