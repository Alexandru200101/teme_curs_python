def numara_cuvinte_fisier(nume_fisier):
    try:
        with open(nume_fisier, 'r') as f:
            text = f.read()
        cuvinte = text.split()  
        return len(cuvinte)
    except FileNotFoundError:
        print(f"Fișierul {nume_fisier} nu a fost găsit.")
        return None

if __name__ == "__main__":
    fisier = "input.txt"
    total_cuvinte = numara_cuvinte_fisier(fisier)
    if total_cuvinte is not None:
        print(f"Fișierul {fisier} conține {total_cuvinte} cuvinte.")
