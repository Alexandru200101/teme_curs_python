def transforma_text_in_majuscule(fisier_intrare, fisier_iesire):
    try:
        with open(fisier_intrare, 'r') as f_in:
            continut = f_in.read()
        continut_mare = continut.upper()
        with open(fisier_iesire, 'w') as f_out:
            f_out.write(continut_mare)
        print(f"Textul din '{fisier_intrare}' a fost scris cu litere mari în '{fisier_iesire}'.")
    except FileNotFoundError:
        print(f"Fișierul '{fisier_intrare}' nu a fost găsit.")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    transforma_text_in_majuscule("input.txt", "output.txt")
