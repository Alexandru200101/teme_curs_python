class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def __str__(self):
        return f"Numele brand-ului este {self.brand} din anul {self.year}"
    
class Car(Vehicle):
        def __init__(self,brand,year,seats):
            super().__init__(brand,year)
            self.seats=seats
        def __str__(self):
            return f"Numele brand-ului este {self.brand}, din anul {self.year} si are {self.seats} locuri"
class Bike(Vehicle):
        def __init__(self,brand,year,speeds):
            super().__init__(brand,year)
            self.speeds=speeds
        def __str__(self):
            return f"Numele brand-ului este {self.brand} din anul {self.year} si are {self.speeds} viteze"
        
if __name__=="__main__":
    vehicle=Vehicle("Porsche",2025)
    car = Car("BMW", 2020, 5)
    bike = Bike("Yamaha", 2018, 7)
    print(vehicle)
    print(car)
    print(bike)
        