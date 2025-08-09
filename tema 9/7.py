from collections import Counter

def se_poate_egalizare(s):
    frecvente = Counter(s)  # dict: caracter -> număr de apariții
    valori = list(frecvente.values())  # lista doar cu frecvențele
    
    if len(valori) == 1:
        return True  # toate caracterele sunt identice
    
    # Caz 1: toate frecvențele sunt deja egale
    if len(set(valori)) == 1:
        return True

    # Caz 2: încercăm eliminarea unei apariții
    for i in range(len(valori)):
        temp = valori.copy()
        temp[i] -= 1  # eliminăm o apariție
        if temp[i] == 0:
            temp.pop(i)  # dacă frecvența ajunge la 0, ștergem caracterul

        if len(set(temp)) == 1:
            return True  # toate frecvențele rămase sunt egale

    return False
s1 = "pptthhh"
s2 = "xyyyzzz"
s3 = "ppttthhh"

print(se_poate_egalizare(s1))  # True
print(se_poate_egalizare(s2))  # True
print(se_poate_egalizare(s3))