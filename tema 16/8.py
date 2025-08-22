class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def __str__(self):
        return f"Persoana: {self.name}, {self.age} ani"

class Student(Person):
    def __init__(self, grades, **kwargs):
        self.grades = grades
        super().__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()}, Note: {self.grades}"

class Teacher(Person):
    def __init__(self, subject, **kwargs):
        self.subject = subject
        super().__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()}, Materie: {self.subject}"

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, grades, subject):
        super().__init__(name=name, age=age, grades=grades, subject=subject)

    def __str__(self):
        return f"{super().__str__()} (Asistent universitar)"

# Utilizare
if __name__ == "__main__":
    p = Person(name="Ion", age=40)
    s = Student(name="Maria", age=20, grades=[9,10,8])
    t = Teacher(name="Ana", age=35, subject="Matematica")
    ta = TeachingAssistant(name="Alex", age=22, grades=[10,9,10], subject="Fizica")

    print(p)
    print(s)
    print(t)
    print(ta)

