# Clasele (folosim varianta corectă de mai devreme)
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Brand-ul masinii este {self.brand} din anul {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    def __str__(self):
        return f"{super().__str__()} si are {self.seats} locuri."

class ElectricCar(Car):
    def __init__(self, brand, year, seats, battery_capacity):
        super().__init__(brand, year, seats)
        self.battery_capacity = battery_capacity

    def calculeaza_range(self):
        return self.battery_capacity * 5

    def __str__(self):
        autonomia = self.calculeaza_range()
        return f"{super().__str__()}\nAutonomia bateriei este de {autonomia} km"



if __name__ == "__main__":
    
    vehicle1 = Vehicle("Dacia", 2015)
    print(vehicle1)
    print("-" * 40)

    
    car1 = Car("BMW", 2020, 5)
    print(car1)
    print("-" * 40)

    
    ecar1 = ElectricCar("Tesla", 2023, 5, 100)
    print(ecar1)
    
