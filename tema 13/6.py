def scrie_linii_invers(in_fisier, out_fisier):
    try:
        with open(in_fisier, 'r') as f_in:
            linii = f_in.readlines()

        linii_inversate = linii[::-1]
        with open(out_fisier, 'w') as f_out:
            f_out.writelines(linii_inversate)

        print(f"Liniile din '{in_fisier}' au fost scrise invers în '{out_fisier}'.")
    except FileNotFoundError:
        print(f"Fișierul '{in_fisier}' nu a fost găsit.")
        
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    scrie_linii_invers("input.txt", "output.txt")
