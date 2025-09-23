import requests

def f(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Eroare: {response.status_code}"
    
url = "https://httpbin.org/get"
parametri = {
    "nume": "Alice",
    "varsta": 25
}

data = f(url, parametri)

if isinstance(data, dict):
    print("URL complet:", data["url"])      
    print("Args:", data["args"])            
else:
    print(data)