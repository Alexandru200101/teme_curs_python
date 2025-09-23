import requests

url = "https://httpbin.org/status/404"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Pagina a fost descărcată cu succes!")
    else:
        print("Eroare: pagina nu a fost găsită")
except requests.RequestException as e:
    print("A apărut o eroare la descărcare:", e)