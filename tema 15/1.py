class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        return self.brand,self.model,self.year
    
if __name__=="__main__":
    car1 = Car("Toyota","Camry",2020)
    print(car1.display_info())
