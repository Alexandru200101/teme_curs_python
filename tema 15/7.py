class Library:
    def __init__(self, author, book=None):
        self.book = book if book is not None else []
        self.author = author

    def add_book(self, carte, author):
        # carte poate fi doar titlul, dar avem nevoie și de autor
        self.book.append({"title": carte, "author": author})
        return f"Cartea {carte} a fost adaugata in biblioteca cu succes. Lista actuala: {self.book}"

    def find_by_author(self, author_name):
        gasite = [b["title"] for b in self.book if b["author"] == author_name]
        if gasite:
            return f"Cărțile autorului {author_name}: {', '.join(gasite)}"
        else:
            return f"Nu există cărți de {author_name} în bibliotecă."


if __name__ == "__main__":
    lib = Library("Biblioteca mea")
    lib.add_book("Critica ratiunii pure", "Kant")
    lib.add_book("Prolegomene", "Kant")
    lib.add_book("Povestea lui Harap-Alb", "Creangă")

    print(lib.find_by_author("Kant"))
    print(lib.find_by_author("Creangă"))
    print(lib.find_by_author("Eminescu"))
