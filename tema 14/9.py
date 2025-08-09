import csv

def elimina_emailuri_duplicate(input_file, output_file):
    try:
        emailuri_unice = set()

        # Citim emailurile din fișier
        with open(input_file, mode='r', encoding='utf-8') as f_in:
            reader = csv.DictReader(f_in)
            for linie in reader:
                email = linie['email'].strip().lower()  # normalizare
                emailuri_unice.add(email)

        # Scriem emailurile unice în fișierul de ieșire
        with open(output_file, mode='w', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out)
            writer.writerow(['email'])  # antet
            for email in sorted(emailuri_unice):  # sortare opțională
                writer.writerow([email])

        print(f"Fișierul '{output_file}' a fost creat cu succes fără duplicate.")

    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except KeyError:
        print("Coloana 'email' lipsește din fișier.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

if __name__ == "__main__":
    elimina_emailuri_duplicate("emailuri.csv", "emailuri_unice.csv")
