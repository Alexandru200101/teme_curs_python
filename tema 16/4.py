import matplotlib
class Shape:
    def area(self):
        raise NotImplementedError("Trebuie implementată în subclasă")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def __str__(self):
        return f"Aria dreptunghiului este {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        return f"Aria cercului este {self.area()}"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return f"Aria triunghiului este {self.area()}"

if __name__=="__main__":
    # shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 2)]

    # for shape in shapes:
    #     print(shape)

    # total = sum(shape.area() for shape in shapes)
    # print("Suma ariilor este:", total)
    while True:
        choice = input("La ce forma geometrica vreti sa aflati aria? \n""(1) Dreptunghi \n(2) Cerc \n(3) Triunghi \n(q) Iesire\n>>> ")

        if choice == "q":
            print("La revedere!")
            break

        elif choice == "1":
            length = float(input("Introduceti lungimea in centimetrii: "))
            width = float(input("Introduceti latimea in centimetrii: "))
            rect = Rectangle(length, width)
            print(rect)

        elif choice == "2":
            radius = float(input("Introduceti raza in centimetrii: "))
            circ = Circle(radius)
            print(circ)

        elif choice == "3":
            base = float(input("Introduceti baza in centimetrii: "))
            height = float(input("Introduceti inaltimea in centimetrii: "))
            tri = Triangle(base, height)
            print(tri)

        else:
            print("Optiune invalida, incearca din nou.")


