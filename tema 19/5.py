import requests
import time

url = "https://httpbin.org/post"
utilizator = input("Introdu numele de utilizator: ")
parola = input("Introdu parola: ")
upload = {"utilizator": utilizator, "parola": parola}

for i in range(3):  
    response = requests.post(url, json=upload)
    if response.status_code == 200:
        print(response.json())
        break
    elif response.status_code == 503:
        print("Server indisponibil, încerc din nou...")
        time.sleep(2)  
    else:
        print("Eroare:", response.status_code)
        break
