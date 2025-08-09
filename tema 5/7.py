# Varianta 1 Iterativă
n = int(input("Introduceti un numar: "))

factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print(f"Factorialul este: {factorial}")

# Varianta 2 Recursivă
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1  
#     else:
#         return n * factorial(n - 1)  


# numar = int(input("Introdu un număr: "))
# rezultat = factorial(numar)
# print(f"Factorialul lui {numar} este: {rezultat}")