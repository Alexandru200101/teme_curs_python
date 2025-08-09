import csv

def actualizeaza_status_studenti(input_file, output_file):
    try:
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            studenti = []

            for linie in reader:
                try:
                    media = float(linie['media'])
                    linie['status'] = 'Promovat' if media > 5 else 'Corigent'
                    studenti.append(linie)
                except ValueError:
                    print(f"Media invalidă pentru elevul: {linie.get('nume')}")

        with open(output_file, mode='w', encoding='utf-8', newline='') as f_out:
            fieldnames = reader.fieldnames + ['status']
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(studenti)

        print(f"Fișierul '{output_file}' a fost creat cu succes.")

    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except KeyError as e:
        print(f"Coloană lipsă: {e}")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    actualizeaza_status_studenti("studenti.csv", "studenti_actualizat.csv")
