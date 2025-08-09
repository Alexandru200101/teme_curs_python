def citeste_numere_si_aduna():
    suma = 0
    while True:
        valoare = input("Introdu un număr (sau 'stop' pentru a opri): ")
        if valoare.lower() == "stop":
            break
        try:
            numar = float(valoare)
            suma += numar
        except ValueError:
            print("Valoare invalidă! Te rog să introduci un număr.")
    return suma


if __name__ == "__main__":
    total = citeste_numere_si_aduna()
    print(f"Suma numerelor introduse este: {total}")
