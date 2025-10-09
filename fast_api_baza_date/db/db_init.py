from db.db_conectare import conectare_baza_date
from db.models.base import Base
from db.models.utilizatori_model import UtilizatoriModel
from db.models.carti_model import CartiModel
from db.models.autori_model import AutoriModel
from db.models.imprumut_model import Imprumut
from sqlalchemy.orm import Session
from db.db_conectare import conectare_baza_date
from db.models.carti_model import CartiModel

# === Creaaza tabelele definite in models ===
def init_db(): 
    engine = conectare_baza_date()
    Base.metadata.create_all(engine)
    print("✅ Toate tabelele au fost create sau există deja.")


def adauga_autori_si_carti():
    engine = conectare_baza_date()
    session = Session(bind=engine)
    autori = [
        "Frank Herbert",            # Dune
        "Jane Austen",              # Mândrie și prejudecată
        "Fyodor Dostoevsky",        # Crimă și pedeapsă
        "George Orwell",            # 1984
        "J.K. Rowling",             # Harry Potter și Piatra Filozofală
        "Antoine de Saint-Exupéry",# Micul Prinț
        "Harper Lee",               # To Kill a Mockingbird
        "Margaret Mitchell",        # Pe aripile vântului
        "J.R.R. Tolkien",           # Stăpânul Inelelor
        "C.S. Lewis",               # Cronicile din Narnia
        "Mihail Bulgakov",          # Maestrul și Margareta
        "Mary Shelley",             # Frankenstein
        "Charlotte Brontë",         # Jane Eyre
        "Bram Stoker",              # Dracula
        "George Orwell",            # Ferma Animalelor
        "Homer",                    # Odiseea
        "Homer",                    # Iliada
        "Miguel de Cervantes",      # Don Quijote
        "Lev Tolstoi",              # Război și pace
        "Charles Dickens",          # Procesul / Marile speranțe
        "Charles Dickens",          # Marile speranțe
        "John Steinbeck",           # Oameni și șoareci
        "Ray Bradbury",             # Fahrenheit 451
        "Jules Verne",              # Călătorie spre centrul Pământului
        "Jules Verne",              # Insula Misterioasă
        "Thomas Hardy",             # Departe de lumea dezlănțuită
        "Herman Melville",          # Moby Dick
        "Victor Hugo",              # Les Misérables
        "Alexandre Dumas",          # Cei trei muschetari
        "William Shakespeare",      # Regele Lear
        "William Shakespeare",      # Hamlet
        "William Shakespeare",      # Macbeth
        "William Shakespeare",      # Othello
        "William Shakespeare",      # Romeo și Julieta
        "Harriet Beecher Stowe",    # Coliba unchiului Tom
        "Oscar Wilde",              # Portretul lui Dorian Gray
        "Marcel Proust",            # În căutarea timpului pierdut
        "Jack Kerouac",             # Pe drum
        "William Faulkner",         # Zgomotul și furia
        "Vladimir Nabokov",         # Lolita
        "Paulo Coelho",             # Alchimistul
        "Dante Alighieri",          # Inferno
        "Dante Alighieri",          # Divina Comedie
        "Henri Charrière",          # Papillon
        "Stephen King",             # Călăuza
        "Nikos Kazantzakis",        # Zorba Grecul
        "Ivan Turgenev",            # Părinții și copiii
        "Lev Tolstoi",              # Anna Karenina
        "John Steinbeck",            # Fructele mâniei
        "Yann Martel"              # Viața lui Pi
    ]

    autor_objs = [AutoriModel(nume = n) for n in autori]
    session.add_all(autor_objs)
    session.commit()

# === Adaugă 50 de cărți în baza de date (fără autori) ===

    carti = [
        {"titlu": "Dune", "gen": "SF", "an_publicare": 1965},
        {"titlu": "Mândrie și prejudecată", "gen": "Romantic", "an_publicare": 1813},
        {"titlu": "Crimă și pedeapsă", "gen": "Psihologic", "an_publicare": 1866},
        {"titlu": "1984", "gen": "Distopie", "an_publicare": 1949},
        {"titlu": "Harry Potter și Piatra Filozofală", "gen": "Fantasy", "an_publicare": 1997},
        {"titlu": "Micul Prinț", "gen": "Ficțiune", "an_publicare": 1943},
        {"titlu": "To Kill a Mockingbird", "gen": "Dramă", "an_publicare": 1960},
        {"titlu": "Pe aripile vântului", "gen": "Romantic", "an_publicare": 1936},
        {"titlu": "Stăpânul Inelelor", "gen": "Fantasy", "an_publicare": 1954},
        {"titlu": "Cronicile din Narnia", "gen": "Fantasy", "an_publicare": 1950},
        {"titlu": "Maestrul și Margareta", "gen": "Fantezie", "an_publicare": 1967},
        {"titlu": "Frankenstein", "gen": "Horror", "an_publicare": 1818},
        {"titlu": "Jane Eyre", "gen": "Romantic", "an_publicare": 1847},
        {"titlu": "Dracula", "gen": "Horror", "an_publicare": 1897},
        {"titlu": "Ferma Animalelor", "gen": "Satiră", "an_publicare": 1945},
        {"titlu": "Odiseea", "gen": "Epic", "an_publicare": -800},
        {"titlu": "Iliada", "gen": "Epic", "an_publicare": -750},
        {"titlu": "Don Quijote", "gen": "Comedie", "an_publicare": 1605},
        {"titlu": "Război și pace", "gen": "Istoric", "an_publicare": 1869},
        {"titlu": "Procesul", "gen": "Psihologic", "an_publicare": 1925},
        {"titlu": "Marile speranțe", "gen": "Dramă", "an_publicare": 1861},
        {"titlu": "Oameni și șoareci", "gen": "Dramă", "an_publicare": 1937},
        {"titlu": "Fahrenheit 451", "gen": "SF", "an_publicare": 1953},
        {"titlu": "Călătorie spre centrul Pământului", "gen": "Aventură", "an_publicare": 1864},
        {"titlu": "Insula Misterioasă", "gen": "Aventură", "an_publicare": 1874},
        {"titlu": "Departe de lumea dezlănțuită", "gen": "Romantic", "an_publicare": 1874},
        {"titlu": "Moby Dick", "gen": "Aventură", "an_publicare": 1851},
        {"titlu": "Les Misérables", "gen": "Dramă", "an_publicare": 1862},
        {"titlu": "Cei trei muschetari", "gen": "Aventură", "an_publicare": 1844},
        {"titlu": "Regele Lear", "gen": "Tragedie", "an_publicare": 1606},
        {"titlu": "Hamlet", "gen": "Tragedie", "an_publicare": 1603},
        {"titlu": "Macbeth", "gen": "Tragedie", "an_publicare": 1606},
        {"titlu": "Othello", "gen": "Tragedie", "an_publicare": 1603},
        {"titlu": "Romeo și Julieta", "gen": "Romantic", "an_publicare": 1597},
        {"titlu": "Coliba unchiului Tom", "gen": "Istoric", "an_publicare": 1852},
        {"titlu": "Portretul lui Dorian Gray", "gen": "Filosofic", "an_publicare": 1890},
        {"titlu": "În căutarea timpului pierdut", "gen": "Psihologic", "an_publicare": 1913},
        {"titlu": "Pe drum", "gen": "Beat", "an_publicare": 1957},
        {"titlu": "Zgomotul și furia", "gen": "Dramă", "an_publicare": 1929},
        {"titlu": "Lolita", "gen": "Psihologic", "an_publicare": 1955},
        {"titlu": "Alchimistul", "gen": "Motivațional", "an_publicare": 1988},
        {"titlu": "Inferno", "gen": "Epic", "an_publicare": 1320},
        {"titlu": "Divina Comedie", "gen": "Epic", "an_publicare": 1321},
        {"titlu": "Papillon", "gen": "Aventură", "an_publicare": 1969},
        {"titlu": "Călăuza", "gen": "SF", "an_publicare": 1972},
        {"titlu": "Zorba Grecul", "gen": "Filosofic", "an_publicare": 1946},
        {"titlu": "Părinții și copiii", "gen": "Dramă", "an_publicare": 1862},
        {"titlu": "Anna Karenina", "gen": "Romantic", "an_publicare": 1878},
        {"titlu": "Fructele mâniei", "gen": "Dramă", "an_publicare": 1939},
        {"titlu": "Viața lui Pi", "gen": "Aventură", "an_publicare": 2001}
    ]

    for c in carti:
        carte = CartiModel(
            titlu=c["titlu"],
            gen=c.get("gen"),
            an_publicare=c.get("an_publicare"),
            autor=c["autor"] # Asignează un autor în mod ciclic
        )
        session.add(carte)

    session.commit()
    session.close()
    print("✅ 50 de cărți au fost adăugate în baza de date (fără autori)!")

    

if __name__ == "__main__":
    adauga_autori_si_carti()