def inmultire(lista1,lista2):
    produs = list(map(lambda x,y:x*y,lista1,lista2))
    return produs

lista1=[1,2,3]
lista2=[4,5,6]
print(inmultire(lista1,lista2))