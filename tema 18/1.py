def transormare(lista):
    if len(lista) == 0:
        print("Lista e goala")
        return []
    else:
        lista_transformata= list(map(lambda x: x.upper(),lista))
        return lista_transformata

lista =["java","python","rust"]
print(f"Lista originala este:{lista}\nLista transformata este: {transormare(lista)}")