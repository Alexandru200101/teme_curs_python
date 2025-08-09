import csv

def numara_angajari(fisier_csv):
    try:
        with open(fisier_csv, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # sari peste antet
            total = sum(1 for _ in reader)
        print(f"Numărul de angajări este: {total}")
    except FileNotFoundError:
        print(f"Fișierul '{fisier_csv}' nu a fost găsit.")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    numara_angajari("angajati.csv")
