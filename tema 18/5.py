def decorator(functia_originala):
    def functie_decorata(*args, **kwargs):
        print("Se execută înainte de funcția originală")
        rezultat = functia_originala(*args, **kwargs)
        print("Se execută după funcția originală")
        return rezultat
    return functie_decorata

@decorator
def salut():
    print("Salut lume!")
salut()




