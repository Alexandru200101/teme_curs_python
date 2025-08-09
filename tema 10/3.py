def combina_liste(*liste):
    rezultat = []
    for lista in liste:
        rezultat.extend(lista)
    return rezultat
a = [1, 2]
b = [3, 4]
c = [5, 6]

rez = combina_liste(a, b, c)
print(*rez)