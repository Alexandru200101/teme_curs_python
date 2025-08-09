a = input("Introduceti ceva: ")

try:
    a = float(a)
    print("Este un numar:", a)
except ValueError:
    print("Nu este un numar, este un text:", a)