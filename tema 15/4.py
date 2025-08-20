class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return f"{self.owner} a depozitat suma de {amount}. Balanta curenta:{self.balance}"
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Fonduri insuficiente! Balanța curentă este {self.balance}"
        else:
            self.balance -= amount
            return f"{self.owner} a retras {amount}. Balanța curentă: {self.balance}"


if __name__ == "__main__":
    acc1 = BankAccount("Ion") 
    print(f"Bun venit, {acc1.owner}! Balanța inițială este {acc1.balance}.\n")

    while True:
        optiune = input("Doriți să depuneți (d), să retrageți (r) sau să ieșiți (x)? ").lower()

        if optiune == "d":
            suma = int(input("Introduceți suma de depus: "))
            print(acc1.deposit(suma))

        elif optiune == "r":
            suma = int(input("Introduceți suma de retras: "))
            print(acc1.withdraw(suma))

        elif optiune == "x":
            print("La revedere! Balanța finală este:", acc1.balance)
            break

        else:
            print("Opțiune invalidă. Încercați din nou.")


