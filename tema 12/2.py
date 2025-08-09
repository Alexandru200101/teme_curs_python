lista = [10, 20, 30, 40, 50]

try:
    index = int(input("Introduceți un index între 0 și 4: "))
    print(f"Elementul de la indexul {index} este: {lista[index]}")
except IndexError:
    print("Eroare: Indexul este în afara listei.")
except ValueError:
    print("Eroare: Trebuie să introduceți un număr întreg.")
