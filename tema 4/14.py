numar = int(input("Introduceti un numar: "))
if numar >= 100:
    suma_cifre = sum(int(cifra) for cifra in str(numar))
    print(f"Suma cifrelor este:", suma_cifre)
elif numar < 100:
    print("python")