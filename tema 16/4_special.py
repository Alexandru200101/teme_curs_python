import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    def plot(self):
        fig, ax = plt.subplots()
        rect = patches.Rectangle((0, 0), self.length, self.width, edgecolor='blue', facecolor='cyan', alpha=0.5)
        ax.add_patch(rect)
        ax.set_xlim(-1, self.length + 1)
        ax.set_ylim(-1, self.width + 1)
        ax.set_aspect('equal')
        ax.set_title("Dreptunghi")
        plt.show()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        return f"Aria cercului este {self.area()}"
    def plot(self):
        fig, ax = plt.subplots()
        circ = patches.Circle((0, 0), radius=self.radius, edgecolor='red', facecolor='orange', alpha=0.5)
        ax.add_patch(circ)
        ax.set_xlim(-self.radius - 1, self.radius + 1)
        ax.set_ylim(-self.radius - 1, self.radius + 1)
        ax.set_aspect('equal')
        ax.set_title("Cerc")
        plt.show()

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return f"Aria triunghiului este {self.area()}"
    def plot(self):
        fig, ax = plt.subplots()
        triangle = patches.Polygon([[0,0],[self.base,0],[self.base/2,self.height]], edgecolor='green', facecolor='yellow', alpha=0.5)
        ax.add_patch(triangle)
        ax.set_xlim(-1, self.base + 1)
        ax.set_ylim(-1, self.height + 1)
        ax.set_aspect('equal')
        ax.set_title("Triunghi")
        plt.show()


if __name__=="__main__":
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
            rect.plot()  

        elif choice == "2":
            radius = float(input("Introduceti raza in centimetrii: "))
            circ = Circle(radius)
            print(circ)
            circ.plot()  

        elif choice == "3":
            base = float(input("Introduceti baza in centimetrii: "))
            height = float(input("Introduceti inaltimea in centimetrii: "))
            tri = Triangle(base, height)
            print(tri)
            tri.plot()  

        else:
            print("Optiune invalida, incearca din nou.")
