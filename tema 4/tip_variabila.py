# Varianta 1 (folosind try-except)

# a = input("Introdu ceva: ")


# try:
#     numar = int(a)
#     print(numar ** 2)
# except ValueError:
#     print("Ai introdus text:", a)

# Varianta 2 (folosind isdigit)

a = input("Introdu ceva: ")

if a.isdigit():
    a = int(a)
    print(f"patratul lui {a} este",a ** 2) 
else:
    print(a)