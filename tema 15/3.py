class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def tip(self):
        if self.pages <= 150:
            return f"Cartea {self.title} este o nuvela"
        else:
            return f"Cartea {self.title} este un roman"

if __name__=="__main__":
    book1=Book("critica ratiunii pure","Kant",300)
    print(book1.tip())