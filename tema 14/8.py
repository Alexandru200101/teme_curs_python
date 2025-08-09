import csv

def genereaza_raport(clienti_file, comenzi_file, raport_file):
    try:
        # Pas 1: Citim clientii si salvam id_client -> nume_client intr-un dictionar
        clienti = {}
        with open(clienti_file, mode='r', encoding='utf-8') as f_clienti:
            reader = csv.DictReader(f_clienti)
            for linie in reader:
                clienti[linie['id_client']] = linie['nume_client']

        # Pas 2: Citim comenzile si inlocuim id_client cu nume_client
        raport_linii = []
        with open(comenzi_file, mode='r', encoding='utf-8') as f_comenzi:
            reader = csv.DictReader(f_comenzi)
            for linie in reader:
                id_client = linie['id_client']
                nume_client = clienti.get(id_client, "Necunoscut")
                raport_linii.append({
                    'id_comanda': linie['id_comanda'],
                    'nume_client': nume_client,
                    'suma': linie['suma'],
                    'data': linie['data']
                })

        # Pas 3: Scriem in raport.csv
        with open(raport_file, mode='w', encoding='utf-8', newline='') as f_raport:
            fieldnames = ['id_comanda', 'nume_client', 'suma', 'data']
            writer = csv.DictWriter(f_raport, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(raport_linii)

        print(f"Raportul a fost generat cu succes în '{raport_file}'.")

    except FileNotFoundError as e:
        print(f"Eroare: Fișierul nu a fost găsit - {e.filename}")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

if __name__ == "__main__":
    genereaza_raport("clienti.csv", "comenzi.csv", "raport.csv")
