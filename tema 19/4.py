import requests

# url = "https://httpbin.org/image/png"
# response = requests.get(url)
# if response.status_code == 200:
    
#     with open("image.png", "wb") as f:
#         f.write(response.content)  
#     print("Poza a fost descărcată cu succes!")
# else:
#     print("Eroare:", response.status_code)

import requests

def f(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return "Poza a fost descărcată cu succes!"
    else:
        return f"Eroare: {response.status_code}"

url = input("Introdu URL-ul imaginii: ")
filename = input("Introdu numele fișierului (ex: poza.png): ")

print(f(url, filename))
    



