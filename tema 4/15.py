propozitie = input("Introduceți o propoziție: ")
propozitie_modificata = propozitie.lower().split()
if propozitie_modificata[0] == "python":
    print(True)
else:
    print(False)
