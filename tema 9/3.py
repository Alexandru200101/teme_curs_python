import random

lista = list(range(1, 50))
loto = set(random.sample(lista, 6))  # extragere, convertită în set

jucator = input("Introduceti 6 numere separate prin spatiu pentru a juca 6/49: ")
jucator_lista = list(map(int, jucator.split()))
jucator_set = set(jucator_lista)  # convertim și numerele jucătorului în set

if len(jucator_lista) != 6:
    print("Trebuie să introduci exact 6 numere!")
elif any(num < 1 or num > 49 for num in jucator_set):
    print("Numerele trebuie să fie între 1 și 49!")
elif len(jucator_set) != 6:
    print("Nu trebuie să repeti numere!")
else:
    print("Numerele tale:", jucator_set)
    print("Numerele extrase:", loto)

    # găsim intersecția - ce numere ai nimerit
    nimerite = jucator_set.intersection(loto)
    print(f"Ai nimerit {len(nimerite)} numere: {nimerite}")


    
    
