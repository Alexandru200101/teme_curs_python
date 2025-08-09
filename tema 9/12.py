lista = []

while True:
    a = input("Introduceti elemente (sau 'stop' pentru a opri): ")
    if a.lower() == "stop":
        break
    try:
        valoare = eval(a)  # transformă '123' în 123, '"abc"' în 'abc', etc.
    except:
        valoare = a
    lista.append(valoare)

if not lista:
    print("Lista este goala")
else:
    print("Lista finala:", lista)

verificare = [isinstance(elem, str) for elem in lista]
print(verificare)


