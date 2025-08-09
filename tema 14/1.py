import csv

def citeste_produse_din_csv(nume_fisier):
    try:
        with open(nume_fisier, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            print("Produse disponibile:")
            for produs in reader:
                print(f"ID: {produs['id']}, Nume: {produs['nume']}, Preț: {produs['pret']} RON")
    except FileNotFoundError:
        print(f"Fișierul '{nume_fisier}' nu a fost găsit.")
    except KeyError as e:
        print(f"Coloană lipsă în fișier: {e}")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    citeste_produse_din_csv("produse.csv")
