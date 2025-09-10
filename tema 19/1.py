import requests

# url = "https://httpbin.org/get"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()  # dict
#     print("Parametri args:", data["args"])            
#     print("IP-ul origin:", data["origin"])           
#     print("URL:", data["url"])                        
#     print("User-Agent:", data["headers"]["User-Agent"])
# else:
#     print("Eroare:", response.status_code)



def f(url):
    response = requests.get(url)
    if response.status_code ==200:
        return response.json()
    else:
        return f"Eroare: {response.status_code}"

url = "https://httpbin.org/get"
data = f(url)

if isinstance(data, dict):    
    print("Parametri args:", data["args"])            
    print("IP-ul origin:", data["origin"])           
    print("URL:", data["url"])                        
    print("User-Agent:", data["headers"]["User-Agent"])
