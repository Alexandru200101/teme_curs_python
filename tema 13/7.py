def scrie_numere_pare(fisier_intrare, fisier_iesire):
    try:
        with open(fisier_intrare, 'r') as f_in, open(fisier_iesire, 'w') as f_out:
            for linie in f_in:
                linie = linie.strip()
                try:
                    numar = int(linie)
                    if numar % 2 == 0:
                        f_out.write(linie + '\n')
                except ValueError:
                    # linia nu e un numar valid, ignoram
                    continue
        print(f"Numerele pare au fost scrise în '{fisier_iesire}'.")
    except FileNotFoundError:
        print(f"Fișierul '{fisier_intrare}' nu a fost găsit.")
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    scrie_numere_pare("numbers.txt", "pare.txt")
