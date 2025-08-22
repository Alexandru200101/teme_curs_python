class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"Angajatul {self.name} are salariu {self.salary}"
    
class Developer(Employee):
    def __init__(self,name,salary,limbaj_programare):
        super().__init__(name,salary)
        self.limbaj_programare=limbaj_programare
    def __str__(self):
        return f"Angajatul {self.name} lucra in limbajul {self.limbaj_programare} cu salar {self.salary}"
class Designer(Employee):
    def __init__(self,name,salary,soft_design):
        super().__init__(name,salary)
        self.soft_design=soft_design
    def __str__(self):
        return f"Angajatul {self.name} lucra in limbajul {self.soft_design} si are salar {self.salary}"
if __name__=="__main__":
    employee=Employee("Alex",5000)
    developer=Developer("Andrei",4000,"python")
    designer=Designer("Mihai",6000,"Angular")

    print(employee)
    print(developer)
    print(designer)