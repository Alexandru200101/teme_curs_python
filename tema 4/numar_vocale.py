propozitie = input("Introduceți o propoziție: ")

vocale = "aeiou"
consoane = "bcdfghjklmnpqrstvwxyz"

numar_vocale = sum(1 for char in propozitie.lower() if char in vocale)
numar_consoane = sum(1 for char in propozitie.lower() if char in consoane)

print(f"Sunt {numar_vocale} vocale în propoziție.")
print(f"Sunt {numar_consoane} consoane în propoziție.")