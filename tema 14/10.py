import csv

def creste_salariu(input_file):
    angajati = []
    try:
        # Citim datele angajatilor
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linie in reader:
                try:
                    salariu = float(linie['salariu'])
                    salariu_nou = round(salariu * 1.10, 2)  # creștem cu 10%
                    linie['salariu'] = str(salariu_nou)
                    angajati.append(linie)
                except ValueError:
                    print(f"Salariu invalid pentru angajatul {linie.get('nume')}")

        # Scriem înapoi în același fișier cu salariile actualizate
        with open(input_file, mode='w', encoding='utf-8', newline='') as f_out:
            fieldnames = ['nume', 'salariu']
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(angajati)

        print(f"Salariile au fost actualizate cu 10% în '{input_file}'.")

    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except KeyError as e:
        print(f"Lipsește coloana: {e}")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

if __name__ == "__main__":
    creste_salariu("angajati.csv")
