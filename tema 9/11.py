cuvant = input("Introduceți un cuvânt: ")

frecvente = {litera: cuvant.count(litera) for litera in set(cuvant)}

print(frecvente)
