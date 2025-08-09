def afiseaza_linii_cu_cuvant(fisier, cuvant):
    try:
        with open(fisier, 'r') as f:
            for linie in f:
                if cuvant.lower() in linie.lower():
                    print(linie, end='')
    except FileNotFoundError:
        print(f"Fișierul '{fisier}' nu a fost găsit.")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    cuvant_cautat = input("Introduceți cuvântul de căutat: ")
    afiseaza_linii_cu_cuvant("text.txt", cuvant_cautat)
