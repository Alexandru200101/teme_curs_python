import csv

def afiseaza_elevi_cu_media_peste_8(fisier_csv):
    try:
        with open(fisier_csv, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            print("Elevi cu media peste 8:")
            for linie in reader:
                try:
                    media = float(linie['media'])
                    if media > 8:
                        print(linie['nume'])
                except ValueError:
                    print(f"Media invalidă pentru elevul: {linie.get('nume', 'Necunoscut')}")
    except FileNotFoundError:
        print(f"Fișierul '{fisier_csv}' nu a fost găsit.")
    except KeyError as e:
        print(f"Coloană lipsă în fișier: {e}")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    afiseaza_elevi_cu_media_peste_8("studenti.csv")
