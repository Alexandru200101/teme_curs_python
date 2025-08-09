def inverseaza_cuvintele(s):
    # Desparte string-ul după spații (orice număr de spații)
    cuvinte = s.split()
    # Inversează lista de cuvinte
    cuvinte_inversate = cuvinte[::-1]
    # Unește cuvintele cu un singur spațiu
    return ' '.join(cuvinte_inversate)

# Exemplu:
s = 'python java        javascript'
print(inverseaza_cuvintele(s))
