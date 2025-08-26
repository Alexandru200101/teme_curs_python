# Cont bancar ( __eq__, __lt__ )
# Creează o clasă BankAccount cu nume și sold.
# Suprascrie __eq__ pentru a compara două conturi după sold.
# Suprascrie __lt__ pentru a permite sortarea conturilor după sold.
# Testează cu o listă de conturi și sorteaz-o.

class BankAccount:
    def __init__(self, nume):
        self.nume = nume
        self.sold = 0

    def __str__(self):
        return f"{self.nume} are sold-ul {self.sold} RON"

    def deposit(self, suma):
        if suma >= 0:
            self.sold += suma
            print(f"{self.nume} a depus {suma} RON. Sold curent: {self.sold} RON")
        else:
            print("Suma trebuie să fie pozitivă!")
    def withdraw(self, suma):
        if 0 < suma <= self.sold:
            self.sold -= suma
            print(f"{self.nume} a retras {suma} RON. Sold curent: {self.sold} RON")
        else:
            print("Suma invalidă sau fonduri insuficiente!")
    def __eq__(self, other):
        return self.sold == other.sold
    def __lt__(self, other):
        return self.sold < other.sold
if __name__ == "__main__":
    conturi = []
    for nume in ["Ion", "Maria", "Alex"]:
        conturi.append(BankAccount(nume))

    
    while True:
        print("\n--- Meniu conturi bancare ---")
        for i, cont in enumerate(conturi):
            print(f"{i}: {cont}")
        print("a - Adaugă bani")
        print("s - Scoate bani")
        print("q - Ieși")
        optiune = input("Alege o opțiune: ").lower()

        if optiune == "q":
            print("La revedere!")
            break
        elif optiune in ["a", "s"]:
            try:
                index = int(input("Selectează contul după index: "))
                cont = conturi[index]
            except (ValueError, IndexError):
                print("Index invalid!")
                continue

            try:
                suma = int(input("Introdu suma: "))
            except ValueError:
                print("Suma trebuie să fie un număr întreg!")
                continue

            if optiune == "a":
                cont.deposit(suma)
            else:
                cont.withdraw(suma)
        else:
            print("Opțiune invalidă! Încearcă din nou.")
    conturi.sort()
    print("\nConturile sortate după sold (crescător):")
    for cont in conturi:
        print(cont)

