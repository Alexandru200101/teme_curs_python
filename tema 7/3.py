math_grades = {'Marius': 8.0,'Andreea': 9.5,'Adrian': 7.9,'Bianca': 10}

# varianta 1: fara comprehensiune
# a = []
# for value in math_grades.values():
#     a.append(value)
#     a.sort()
# print(f" nota cea mai mare din dictionar este: {max(a)}")
# print(f"notele in ordine crescatoare sunt: {a}")






# # varianta 2: cu comprehensiune
# a = max(value for value in math_grades.values())  #Cream un generator pentru a gasi nota maxima
# print(f"nota cea mai mare din dictionar este: {a}")
# print(f"notele in ordine crescatoare sunt: {sorted(math_grades.values())}")

# Varianta 3: folosind sortarea direct pe valorile din dicționar
# Extragem valorile (notelor), le sortăm și le analizăm
note = sorted(math_grades.values())

# Nota maximă este ultima în lista sortată
nota_maxima = note[-1] if note else None

print(f"Notele în ordine crescătoare sunt: {note}")
print(f"Nota cea mai mare din dicționar este: {nota_maxima}")