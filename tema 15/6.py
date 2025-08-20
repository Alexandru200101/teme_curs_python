class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Angajat: {self.name}, salariu: {self.salary} lei"


class Manager(Employee):
    def __init__(self, name, salary, employees=None):
        super().__init__(name, salary)
        self.employees = employees if employees is not None else []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_team(self):
        if not self.employees:
            return f"{self.name} nu are angajați în subordine."
        else:
            lista = ", ".join(emp.name for emp in self.employees)
            return f"{self.name} coordonează: {lista}"

    def __str__(self):
        return f"Manager: {self.name}, salariu: {self.salary} lei, nr. angajați: {len(self.employees)}"
    

if __name__ == "__main__":
    e1 = Employee("Ion", 3000)
    e2 = Employee("Maria", 3200)
    e3 = Employee("George", 2800)

    m1 = Manager("Ana", 6000)
    m1.add_employee(e1)
    m1.add_employee(e2)
    m1.add_employee(e3)

    print(e1)
    print(m1)
    print(m1.show_team())
