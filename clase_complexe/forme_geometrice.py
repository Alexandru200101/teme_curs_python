import math
import matplotlib.pyplot as plt
import numpy as np

# Clasa principală care gestionează formele geometrice
class Geometric:
    def __init__(self, tip):
        self.tip = tip

    def __str__(self):
        return f"Tipul formei geometrice este {self.tip}"

class Forma:
    def __init__(self, tip, laturi=None, radius=None):
        self.tip = tip
        self.laturi = laturi if laturi is not None else []
        self.radius = radius

    def determinare_forma(self):
        # Dacă avem doar o singură valoare, o considerăm o formă geometrică validă
        if len(self.laturi) == 1:  # Cazul când avem o formă cu o singură latură (pătrat, hexagon etc.)
            if self.tip == "hexagon":
                return self.Hexagon(self.laturi[0]).arie()
            elif self.tip == "patrat":
                return self.Patrat(self.laturi[0]).verificare()
            elif self.tip == "pentagon":
                return self.Pentagon(self.laturi[0]).arie()
            elif self.tip == "heptagon":
                return self.Heptagon(self.laturi[0]).arie()
            else:
                print("Nu este o formă geometrică validă!")
                return None
        elif len(self.laturi) == 3:
            return self.Triunghi(self.laturi[0], self.laturi[1], self.laturi[2]).calcul_arie()
        elif len(self.laturi) == 4:
            return self.Patrat(self.laturi[0]).verificare()
        elif len(self.laturi) == 5:
            return self.Pentagon(self.laturi[0]).arie()
        elif len(self.laturi) == 6:
            return self.Hexagon(self.laturi[0]).arie()
        elif len(self.laturi) == 7:
            return self.Heptagon(self.laturi[0]).arie()
        elif len(self.laturi) > 7:
            return self.Poligon(len(self.laturi), self.laturi[0]).arie()
        else:
            return "Număr de laturi nevalid!"

    class Triunghi:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
            self.p = (a + b + c) / 2

        def calcul_arie(self):
            # Verifică dacă triunghiul este valid
            if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                area = math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
                self.plotare_triunghi()
                return f"Aria triunghiului este {area:.2f}"
            else:
                return "Laturile nu formează un triunghi valid!"

        def plotare_triunghi(self):
            # Desenăm triunghiul
            plt.figure()
            # Folosim coordonate pentru a crea un triunghi vizual corect
            angle = math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
            x = [0, self.b, self.c * math.cos(angle)]
            y = [0, 0, self.c * math.sin(angle)]
            plt.fill(x, y, "b", alpha=0.5)
            plt.plot(x + [x[0]], y + [y[0]], "r-")
            plt.title("Triunghi")
            plt.axis('equal')
            plt.grid(True)
            plt.show()

    class Patrat:
        def __init__(self, latura):
            self.latura = latura

        def verificare(self):
            self.plotare_patrat()
            return f"Aria patratului este {self.latura ** 2}"

        def plotare_patrat(self):
            # Desenăm pătratul
            plt.figure()
            x = [0, self.latura, self.latura, 0, 0]
            y = [0, 0, self.latura, self.latura, 0]
            plt.fill(x, y, "g", alpha=0.5)
            plt.plot(x, y, "r-")
            plt.title("Patrat")
            plt.axis('equal')
            plt.grid(True)
            plt.show()

    class Pentagon:
        def __init__(self, latura):
            self.latura = latura

        def arie(self):
            area = (5 * self.latura ** 2) / (4 * math.tan(math.pi / 5))
            self.plotare_pentagon()
            return f"Aria pentagonului este {area:.2f}"

        def plotare_pentagon(self):
            # Desenăm pentagonul (5 laturi)
            plt.figure()
            x = [self.latura * math.cos(2 * math.pi * i / 5 + math.pi/2) for i in range(5)]
            y = [self.latura * math.sin(2 * math.pi * i / 5 + math.pi/2) for i in range(5)]
            plt.fill(x, y, "y", alpha=0.5)
            plt.plot(x + [x[0]], y + [y[0]], "r-")
            plt.title("Pentagon")
            plt.axis('equal')
            plt.grid(True)
            plt.show()

    class Hexagon:
        def __init__(self, latura):
            self.latura = latura

        def arie(self):
            area = (3 * math.sqrt(3) / 2) * self.latura ** 2
            self.plotare_hexagon()
            return f"Aria hexagonului este {area:.2f}"

        def plotare_hexagon(self):
            # Desenăm hexagonul
            plt.figure()
            x = [self.latura * math.cos(2 * math.pi * i / 6 + math.pi/2) for i in range(6)]
            y = [self.latura * math.sin(2 * math.pi * i / 6 + math.pi/2) for i in range(6)]
            plt.fill(x, y, "c", alpha=0.5)
            plt.plot(x + [x[0]], y + [y[0]], "r-")
            plt.title("Hexagon")
            plt.axis('equal')
            plt.grid(True)
            plt.show()

    class Heptagon:
        def __init__(self, latura):
            self.latura = latura

        def arie(self):
            area = (7 * self.latura ** 2) / (4 * math.tan(math.pi / 7))
            self.plotare_heptagon()
            return f"Aria heptagonului este {area:.2f}"

        def plotare_heptagon(self):
            # Desenăm heptagonul
            plt.figure()
            x = [self.latura * math.cos(2 * math.pi * i / 7 + math.pi/2) for i in range(7)]
            y = [self.latura * math.sin(2 * math.pi * i / 7 + math.pi/2) for i in range(7)]
            plt.fill(x, y, "m", alpha=0.5)
            plt.plot(x + [x[0]], y + [y[0]], "r-")
            plt.title("Heptagon")
            plt.axis('equal')
            plt.grid(True)
            plt.show()

    class Poligon:
        def __init__(self, numar_laturi, latura):
            self.numar_laturi = numar_laturi
            self.latura = latura

        def arie(self):
            area = (self.numar_laturi * self.latura ** 2) / (4 * math.tan(math.pi / self.numar_laturi))
            self.plotare_poligon()
            return f"Aria poligonului cu {self.numar_laturi} laturi este {area:.2f}"

        def plotare_poligon(self):
            # Desenăm poligonul cu număr de laturi dat
            plt.figure()
            x = [self.latura * math.cos(2 * math.pi * i / self.numar_laturi + math.pi/2) for i in range(self.numar_laturi)]
            y = [self.latura * math.sin(2 * math.pi * i / self.numar_laturi + math.pi/2) for i in range(self.numar_laturi)]
            plt.fill(x, y, "orange", alpha=0.5)
            plt.plot(x + [x[0]], y + [y[0]], "r-")
            plt.title(f"Poligon cu {self.numar_laturi} laturi")
            plt.axis('equal')
            plt.grid(True)
            plt.show()

# Funcția principală pentru interacțiune
def main():
    print("Bine ai venit! Vom calcula aria unei forme geometrice.")
    forma_tip = input("Introdu tipul formei geometrice (Triunghi, Patrat, Pentagon, Hexagon, Heptagon, Poligon): ").lower()

    # Solicită laturile pentru fiecare formă
    if forma_tip in ['hexagon', 'patrat', 'pentagon', 'heptagon']:
        laturi = [float(input(f"Introdu latura {forma_tip}ului: "))]
    elif forma_tip == 'triunghi':
        laturi = list(map(float, input("Introdu laturile triunghiului (3 valori separate prin spațiu): ").split()))
        if len(laturi) != 3:
            print("Trebuie să introduci exact 3 laturi!")
            return
    elif forma_tip == 'poligon':
        numar_laturi = int(input("Introdu numărul de laturi: "))
        latura = float(input("Introdu lungimea laturii: "))
        laturi = [latura] * numar_laturi
    else:
        print("Forma geometrică nu este recunoscută!")
        return

    # Creăm instanța formei
    forma = Forma(forma_tip, laturi, None)
    result = forma.determinare_forma()
    if result:
        print(result)

if __name__ == "__main__":
    main()









