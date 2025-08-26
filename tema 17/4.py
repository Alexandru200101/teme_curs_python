# # Fracții ( __add__, __mul__, __truediv__ )
# # Creează o clasă Fraction cu numărător și numitor.
# # Suprascrie operatorii +, *, /.

# class Calculator:
#     def __init__(self, a):
#         self.a = a

#     def __add__(self, other):
#         return Calculator(self.a + other.a)

#     def __sub__(self, other):
#         return Calculator(self.a - other.a)

#     def __mul__(self, other):
#         return Calculator(self.a * other.a)

#     def __truediv__(self, other):
#         try:
#             return Calculator(self.a / other.a)
#         except ZeroDivisionError:
#             print("Eroare: Împărțire la 0!")
#             return None

#     def __str__(self):
#         return str(self.a)


# if __name__ == "__main__":
#     while True:
#         x_input = input("Introduceti primul numar (sau 'q' pentru iesire): ")
#         if x_input.lower() == "q":
#             print("La revedere!")
#             break
#         try:
#             x = Calculator(float(x_input))
#         except ValueError:
#             print("Trebuie sa introduci un numar valid!")
#             continue

#         y_input = input("Introduceti al doilea numar: ")
#         try:
#             y = Calculator(float(y_input))
#         except ValueError:
#             print("Trebuie sa introduci un numar valid!")
#             continue

#         print("\nOperatii disponibile:")
#         print("a - aduna")
#         print("s - scade")
#         print("m - inmulteste")
#         print("i - imparte")

#         optiune = input("Alege o optiune: ").lower()

#         if optiune == "a":
#             print(f"Rezultatul adunarii este: {x + y}")
#         elif optiune == "s":
#             print(f"Rezultatul scaderii este: {x - y}")
#         elif optiune == "m":
#             print(f"Rezultatul inmultirii este: {x * y}")
#         elif optiune == "i":
#             rezultat = x / y
#             if rezultat is not None:
#                 print(f"Rezultatul impartirii este: {rezultat}")
#         else:
#             print("Optiune invalida!")
import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Numitorul nu poate fi 0!")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Nu se poate împărți la zero!")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
if __name__=="__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    print(f"f1 + f2 = {f1 + f2}")  
    print(f"f1 * f2 = {f1 * f2}")  
    print(f"f1 / f2 = {f1 / f2}")  

