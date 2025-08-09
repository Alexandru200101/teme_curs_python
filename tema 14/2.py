import csv

def scrie_note_in_csv(nume_fisier):
    note = [
        {"nume_elev": "Andrei Pop", "materie": "Matematica", "nota": 9},
        {"nume_elev": "Maria Ionescu", "materie": "Romana", "nota": 10},
        {"nume_elev": "Elena Georgescu", "materie": "Informatica", "nota": 8},
        {"nume_elev": "Radu Marinescu", "materie": "Fizica", "nota": 7},
        {"nume_elev": "Ioana Dinu", "materie": "Biologie", "nota": 10}
    ]

    try:
        with open(nume_fisier, mode='w', newline='', encoding='utf-8') as f:
            coloane = ["nume_elev", "materie", "nota"]
            writer = csv.DictWriter(f, fieldnames=coloane)

            writer.writeheader()  # scrie prima linie (cap de tabel)
            writer.writerows(note)  # scrie toate cele 5 înregistrări

        print(f"Fișierul '{nume_fisier}' a fost creat cu succes.")
    except Exception as e:
        print(f"Eroare la scrierea fișierului: {e}")

if __name__ == "__main__":
    scrie_note_in_csv("note.csv")
