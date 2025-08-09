numar = int(input("Introduceti un numar de 4 cifre: "))

if numar < 1000 or numar > 9999:
    print("Numarul nu are 4 cifre.")
else:
    numar += 1  # Începem cu următorul număr
    while numar <= 9999:
        cifre = str(numar)
        if len(set(cifre)) == 4:  # toate cifrele sunt distincte
            print("Urmatorul numar cu cifre distincte este:", numar)
            break
        numar += 1


