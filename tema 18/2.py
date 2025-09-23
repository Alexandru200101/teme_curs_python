def lungime(lista):
    l = list(map(lambda x:len(x),lista))
    return l

lista = ["java","python","rust"]
print(lungime(lista))