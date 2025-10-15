import numpy as np

def operatii(a, b):
    suma = a + b
    produs = a * b
    patrat = a ** 2
    scalar = np.dot(a, b)
    return f"Suma: {suma}\n Produs: {produs}\n Patrat: {patrat}\n Scalar: {scalar}"


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(operatii(a, b))