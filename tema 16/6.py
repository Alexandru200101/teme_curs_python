class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Autorul cărții '{self.title}' este {self.author}"

class Ebook(Book):
    def __init__(self, title, author, file_size, format):
        super().__init__(title, author)
        self.file_size = file_size
        self.format = format

    def __str__(self):
        
        return f"{super().__str__()}.\nFormat: {self.format}, Dimensiune fișier: {self.file_size}MB"

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def __str__(self):
        if not self.books:
            return "Biblioteca este goală."
        return "\n\n".join(str(book) for book in self.books)

if __name__ == "__main__":
    biblioteca = Library()


    biblioteca.add_book(Book("Micul Prinț", "Antoine de Saint-Exupéry"))
    biblioteca.add_book(Ebook("1984", "George Orwell", 2.5, "PDF"))
    biblioteca.add_book(Ebook("Harry Potter", "J.K. Rowling", 1.8, "EPUB"))

    print("Toate cărțile din bibliotecă:")
    print(biblioteca)

    print("\nCăutare după autor 'George Orwell':")
    for book in biblioteca.search_by_author("George Orwell"):
        print(book)

