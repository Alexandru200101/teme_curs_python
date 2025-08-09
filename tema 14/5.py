import csv

def produse_peste_100_lei(fisier_csv):
    try:
        with open(fisier_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            print("Produse cu valoare totală > 100 lei:\n")
            for linie in reader:
                try:
                    cantitate = int(linie['cantitate'])
                    pret = float(linie['pret_unitar'])
                    valoare_totala = cantitate * pret
                    if valoare_totala > 100:
                        produs = linie['produs']
                        print(f"{produs} → {valoare_totala:.2f} lei")
                except ValueError:
                    print(f"Date invalide în linia: {linie}")
    except FileNotFoundError:
        print(f"Fișierul '{fisier_csv}' nu a fost găsit.")
    except KeyError as e:
        print(f"Lipsă coloană: {e}")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    produse_peste_100_lei("vanzari.csv")
