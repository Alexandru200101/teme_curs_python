import csv
from collections import defaultdict

def calculeaza_total_pe_categorie(input_file, output_file):
    total_pe_categorie = defaultdict(float)

    try:
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linie in reader:
                try:
                    categorie = linie['categorie']
                    suma = float(linie['suma'])
                    total_pe_categorie[categorie] += suma
                except ValueError:
                    print(f"Valoare invalidă pentru suma: {linie.get('suma')}")

        with open(output_file, mode='w', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out)
            writer.writerow(['categorie', 'total'])
            for categorie, total in total_pe_categorie.items():
                writer.writerow([categorie, f"{total:.2f}"])

        print(f"Rezultatul a fost salvat în '{output_file}'.")

    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except KeyError as e:
        print(f"Coloană lipsă: {e}")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

if __name__ == "__main__":
    calculeaza_total_pe_categorie("cheltuieli.csv", "total_pe_categorie.csv")
