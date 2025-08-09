info_grades = {
    'Maria': [8, 9, 10],
    'Bogdan': [8.6, 7.3, 9.9, 10],
    'Ilinca': [10, 10],
    'Andra': [9.5, 7, 9],
    'Daniel': [6, 10, 9.7],
    'Alex': [10, 10]
}

# lista1 = [nume for nume,note in info_grades.items() if len(note) == 3]
# print(lista1)

# for values in info_grades.values():
#     if len(values) == 3:
#         print(tuple(values))

dictionar = {nume: sum(note) /len(note) for nume,note in info_grades.items() } # dict comprehension
print(dictionar)

medie_maxima = max(dictionar.values())  
lista_maxime = [nume for nume, medie in dictionar.items() if medie == medie_maxima]
print(f"Media cea mai mare este: {medie_maxima} al elevului/elevei {', '.join(lista_maxime)}")


# dictionar = {}
# for key, values in info_grades.items():
#     dictionar[key] = sum(values) / len(values)
# print(dictionar)


# Sortăm dicționarul după valori  #folosind funcția sorted cu lambda

# sorted_dictionar = dict(sorted(dictionar.items(), key=lambda item: item[1], reverse=True))
# print(sorted_dictionar)
# print(f"Media cea mai mare este: {sorted_dictionar[list(sorted_dictionar.keys())[0]]} al elevului/elevei {list(sorted_dictionar.keys())[0]}")

# lista_medii = []
# for item in dictionar.items():
#     lista_medii.append(item)

# # Sortare descrescătoare manuală prin selecție
# n = len(lista_medii)
# for i in range(n):
#     max_idx = i
#     for j in range(i+1, n):
#         if lista_medii[j][1] > lista_medii[max_idx][1]:
#             max_idx = j
#     lista_medii[i], lista_medii[max_idx] = lista_medii[max_idx], lista_medii[i]

# # Afișăm elevul cu media cea mai mare
# cel_mai_bun = lista_medii[0]
# print(f"Media cea mai mare este: {cel_mai_bun[1]:.2f} al elevului/elevei {cel_mai_bun[0]}")
