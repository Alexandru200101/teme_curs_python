lista1 = input("Introdu elementele listei 1 separate prin spațiu: ").split()
lista2 = input("Introdu elementele listei 2 separate prin spațiu: ").split()

set1 = set(lista1)
set2 = set(lista2)

comune = set1.intersection(set2)
doar_in_1 = set1.difference(set2)

print("Elementele comune sunt:", comune)
print("Elementele care sunt doar în lista 1:", doar_in_1)


             
