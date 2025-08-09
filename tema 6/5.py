# # Varianta 1
# def are_cifre_distincte(n):
#     cifre = str(n)
#     return len(set(cifre)) == 4

# # Citește un număr de la tastatură
# n = int(input("Introdu un număr de 4 cifre: "))

# # Verificăm următorul număr cu toate cifrele diferite
# n += 1
# while n <= 9999:
#     if are_cifre_distincte(n):
#         print(f"Următorul număr cu toate cifrele distincte este: {n}")
#         break
#     n += 1



# Varianta 2
n = int(input("Introdu un număr de 4 cifre: "))

n += 1
while n <= 9999:
    a = n // 1000           # prima cifră (mii)
    b = n // 100 % 10       # a doua cifră (sute)
    c = n // 10 % 10        # a treia cifră (zeci)
    d = n % 10              # a patra cifră (unități)

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print("Următorul număr cu cifre distincte este:", n)
        break
    n += 1