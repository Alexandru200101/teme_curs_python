# Varianta 2
propozitie = input("Introdu o propozitie: ") 

# Spargem propozitia in cuvinte
cuvinte = propozitie.split()

# Pastram doar cuvintele care NU incep cu 'A' sau 'a'
cuvinte_filtrate = [cuvant for cuvant in cuvinte if not cuvant.startswith(('A', 'a'))]

# Refacem propozitia
propozitie_noua = ' '.join(cuvinte_filtrate)

print("Propozitia fara cuvintele care incep cu 'A' sau 'a':")
print(propozitie_noua)

propozitie = input("Introdu o propozitie: ")

# Spargem propozitia in cuvinte
cuvinte = propozitie.split()

# Cream o lista goala pentru cuvintele filtrate
cuvinte_filtrate = []


# Varianta 2
# # Parcurgem fiecare cuvant si verificam daca NU incepe cu 'A' sau 'a'
# for cuvant in cuvinte:
#     if not cuvant.startswith('A') and not cuvant.startswith('a'):
#         cuvinte_filtrate.append(cuvant)

# # Refacem propozitia
# propozitie_noua = ' '.join(cuvinte_filtrate)

# print("Propozitia fara cuvintele care incep cu 'A' sau 'a':")
# print(propozitie_noua)

