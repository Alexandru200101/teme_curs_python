timp = int(input("Introdu timpul t (în minute): "))

timp_mod = timp % 5

if timp_mod < 3:
    print("semaforul este verde")
else:
    print("semaforul este rosu")
