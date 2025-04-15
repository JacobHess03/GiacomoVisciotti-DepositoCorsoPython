class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        print(f"Il libro si intitola: {self.titolo} ed è stato scritto da: {self.autore} con codice: {self.isbn} ")
        