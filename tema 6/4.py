# list1 = [5, 3, 100, 1, 435, 1000]   Varianta 1(caz particular)
# list1.sort()  # sortăm lista în ordine crescătoare
# print("Lista sortată:", list1)
# print(f" suma primelor 2 cele mai mici numere este: {list1[0] + list1[1]}")  # afișăm suma primelor două numere

# list2 = [1, -4, 10, 18, -53, -33]
# list2_ordonat = [i for i in list2 if i > 0]  # filtrăm numerele pozitive
# list2_ordonat.sort()  
# print(f"suma celor mai mici 2 numere pozitive este: {list2_ordonat[0] + list2_ordonat[1]}")  # afișăm suma primelor două numere pozitive



# Varianta 2 (generală)
# Această funcție primește o listă de numere și returnează suma celor mai mici `cate` numere din listă.
def suma_cele_mai_mici(lista, cate=2, doar_pozitive=False):
    if doar_pozitive:
        lista_filtrata = []
        for numar in lista:
            if numar > 0:
                lista_filtrata.append(numar)
    else:
        lista_filtrata = lista[:]

    if len(lista_filtrata) < cate:
        return "Lista nu are suficiente elemente."

    lista_filtrata.sort()
    suma = 0
    for i in range(cate):
        suma += lista_filtrata[i]

    return suma

list1 = [5, 3, 100, 1, 435, 1000]
print("Suma celor mai mici 2:", suma_cele_mai_mici(list1))  # → 1 + 3 = 4

list2 = [1, -4, 10, 18, -53, -33]
print("Suma celor mai mici 2 pozitive:", suma_cele_mai_mici(list2, cate=2, doar_pozitive=True))  # → 1 + 10 = 11

list3 = [-5, -10, -1]
print("Suma celor mai mici 2:", suma_cele_mai_mici(list3))  # → -10 + -5 = -15

