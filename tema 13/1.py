def numara_linii_fisier(nume_fisier):
    try:
        with open(nume_fisier, 'r') as f:
            linii = f.readlines()
        return len(linii)
    except FileNotFoundError:
        print(f"Fișierul {nume_fisier} nu a fost găsit.")
        return None

if __name__ == "__main__":
    fisier = "input.txt"
    total_linii = numara_linii_fisier(fisier)
    if total_linii is not None:
        print(f"Fișierul {fisier} are {total_linii} linii.")
