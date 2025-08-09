propozitie = input("Introduceti o propozitie: ")

# definim setul consoanelor (doar literele mici)
consoane = set("bcdfghjklmnpqrstvwxzșţ")

# facem un set cu toate literele din propoziție, filtrând doar consoanele
consoane_gasite = {litera.lower() for litera in propozitie if litera.lower() in consoane}

print(f"Consoanele distincte din propozitie sunt: {consoane_gasite}")

