def concatenare(lista1,lista2):
    # c = list(map(lambda x, y: x +" "+ y,lista1,lista2))
    # return c
    return [x + " " + y for x, y in zip(lista1, lista2)]

lista1 = ["Ion", "Maria", "Andrei"]
lista2 = ["Popescu", "Ionescu", "Georgescu"]
print(concatenare(lista1,lista2))