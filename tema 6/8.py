 # Varianta 1
def medie_lungimi(cuvinte):
    
    lungimi = [len(cuvant) for cuvant in cuvinte]
    return sum(lungimi) / len(lungimi)

def cuvinte_mai_lungi(cuvinte):
    medie = medie_lungimi(cuvinte)
    return [cuvant for cuvant in cuvinte if len(cuvant) > medie]

# Exemplu de utilizare:
propozitie = input("Introdu o propozitie: ")
lista_cuvinte = propozitie.split()

rezultat = cuvinte_mai_lungi(lista_cuvinte)
print("Cuvinte mai lungi decât media:", rezultat)


# Varianta 2

# propozitie = input("Introdu o propozitie: ")
# lista_cuvinte = propozitie.split()

# # Calculăm lungimile cuvintelor și suma lor
# suma_lungimi = 0
# for cuvant in lista_cuvinte:
#     suma_lungimi += len(cuvant)

# # Calculăm media lungimilor
# media = suma_lungimi / len(lista_cuvinte)

# # Construim lista cuvinte mai lungi decât media (fără list comprehension)
# cuvinte_mai_lungi = []
# for cuvant in lista_cuvinte:
#     if len(cuvant) > media:
#         cuvinte_mai_lungi.append(cuvant)

# print("Cuvinte mai lungi decât media:", cuvinte_mai_lungi)