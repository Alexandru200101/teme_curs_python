class Student:
    def __init__(self,name,age,grades=None):
        self.name=name
        self.age=age
        self.grades=grades if grades is not None else []
    def adauga_nota(self,nota):
        self.grades.append(nota)
        return f"Nota {nota} a fost adaugata. Notele curente sunt:{self.grades} "
    def calculeaza_media(self):
        if len(self.grades) == 0:
            return "Studentul nu are note."
        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    s1 = Student("Ana", 20)
    print(s1.adauga_nota(9))
    print(s1.adauga_nota(7))
    print("Media notelor este:", s1.calculeaza_media())    
