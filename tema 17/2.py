# Lista personalizată ( __len__ și __getitem__ )
# Creează o clasă MyList care să conțină o listă internă.
# Implementează __len__ ca să returneze lungimea listei.
# Implementează __getitem__ pentru a permite accesul prin [].
# Implementează __contains__ ca să poți verifica if x in lista.

class MyList:
    def __init__(self, lista=None):
        
        self.lista = [] if lista is None else lista

    def patrat(self, start, end):
        try:
            start = complex(start)
            end = complex(end)
            if start.imag != 0 or end.imag != 0 or start.real != int(start.real) or end.real != int(end.real):
                self.lista = [start**2, end**2] 
            else:
                self.lista = [i**2 for i in range(int(start.real), int(end.real)+1)]
        except Exception as e:
            print("Eroare la calculul pătratelor:", e)
            self.lista = []

    def __len__(self):
        return len(self.lista)

    def __getitem__(self, index):
        return self.lista[index]

    def __contains__(self, item):
        return item in self.lista

    def __str__(self):
        return str(self.lista)



if __name__ == "__main__":
    m = MyList()
    while True:
        try:
            start = input("De la ce număr vrei să faci pătratul? (poate fi int, float sau complex, ex: 2+3j) ")
            end = input("Până la ce număr? (poate fi int, float sau complex) ")
            m.patrat(start, end)
            print("Lista de pătrate:", m)
            break
        except ValueError:
            print("Te rog introdu un număr valid!")
        except Exception as e:
            print("A apărut o eroare:", e)
    while True:
        try:
            index = int(input("Ce index vrei să afli din lista? "))
            print("Valoarea de la indexul", index, "este:", m[index])
            break
        except (ValueError, IndexError):
            print("Index invalid! Încearcă din nou.")
    while True:
        try:
            item_input = input("Ce număr cauți în lista? (poate fi int, float sau complex) ")
            item = complex(item_input)
            print("Numărul se află în lista?", item in m)
            break
        except ValueError:
            print("Te rog introdu un număr valid!")
    print("Lungimea listei este:", len(m))

