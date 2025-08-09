numar = abs(int(input("Introdu un număr: ")))

suma_cifre = 0
while numar > 0:
    suma_cifre += numar % 10
    numar //= 10

print(f"Suma cifrelor este: {suma_cifre}")

if suma_cifre % 8 == 0:
    print("Suma cifrelor este divizibilă cu 8.")
else:
    print("Suma cifrelor NU este divizibilă cu 8.")