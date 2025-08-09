def dupa_nume(x):
    return x[0]

def dupa_varsta(x):
    return x[1]

def dupa_inaltime(x):
    return x[2]

def sorteaza_persoane(persoane):
    sortate_dupa_nume = sorted(persoane, key=dupa_nume)
    print("Dupa nume:", sortate_dupa_nume)

    sortate_dupa_varsta = sorted(persoane, key=dupa_varsta)
    print("Dupa varsta:", sortate_dupa_varsta)

    sortate_dupa_inaltime = sorted(persoane, key=dupa_inaltime)
    print("Dupa inaltime:", sortate_dupa_inaltime)

# Exemplu de apel:
persoane = [
    ("Dan", 33, 170),
    ("Mihai", 20, 180),
    ("Daniel", 40, 173)
]

sorteaza_persoane(persoane)
