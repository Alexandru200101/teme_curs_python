#Varianta 1 
# text = input("Introduceti un text: ")

# distinct_characters = set(text) #Transformam textul intr-un set deoarece acesta nu permite duplicitatea
# print("Caractere distincte:", distinct_characters)


#Varianta 2
propozitie = input("Scrie o propoziție: ")
fara_duplicate = ""

for caracter in propozitie:
    if caracter not in fara_duplicate:
        fara_duplicate += caracter

print("Rezultatul fără duplicate:", fara_duplicate)
    

   
    