def scrie_in_fisier(nume_fisier, text):
    try:
        with open(nume_fisier, 'w') as f:
            f.write(text)
        print(f"Textul a fost scris în fișierul {nume_fisier}.")
    except Exception as e:
        print(f"Eroare la scrierea în fișier: {e}")

if __name__ == "__main__":
    sir = input("Introduceți un text: ")
    scrie_in_fisier("output.txt", sir)
