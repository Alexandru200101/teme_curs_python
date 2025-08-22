class Animal:
    def make_sound(self):
        return "Generic sound"


class Dog(Animal):
    def make_sound(self):
        return "Ham Ham!"


class Cat(Animal):
    def make_sound(self):
        return "Miau Miau!"


class Cow(Animal):
    def make_sound(self):
        return "Muuu!"



animals = [Dog(), Cat(), Cow(), Dog(), Cat()]

if __name__=="__main__":
    for animal in animals:
        print(animal.make_sound())


