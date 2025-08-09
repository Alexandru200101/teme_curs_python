def descompune_numar(numar):
    numar_str = str(numar)
    lungime = len(numar_str)
    parti = []

    for i, cifra in enumerate(numar_str):
        if cifra != '0':
            # Puterea lui 10 pentru poziția curentă
            putere = lungime - i - 1
            valoare = int(cifra) * (10 ** putere)
            parti.append(str(valoare))

    return " + ".join(parti)
print(descompune_numar(37))     
print(descompune_numar(114))    
print(descompune_numar(30165))