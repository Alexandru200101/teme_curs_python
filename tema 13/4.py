def copiaza_fisier(sursa, destinatie):
    try:
        with open(sursa, 'r') as f_in:
            continut = f_in.read()
        with open(destinatie, 'w') as f_out:
            f_out.write(continut)
        print(f"Conținutul din '{sursa}' a fost copiat în '{destinatie}'.")
    except FileNotFoundError:
        print(f"Fișierul sursă '{sursa}' nu a fost găsit.")
    except Exception as e:
        print(f"Eroare la copierea fișierului: {e}")

if __name__ == "__main__":
    copiaza_fisier("source.txt", "destination.txt")
