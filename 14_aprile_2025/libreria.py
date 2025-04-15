import libro
titolo = ""
autore = ""
isbn = ""
l1 = libro.Libro(titolo, autore, isbn)

class Libreria:
    catalogo = []
    def __init__(self):
        self.catalogo = []
    
    def aggiungi_libro(self, l1):
        for libro in self.catalogo:
            if libro.isbn == l1.isbn:
                print("Il libro è già presente.")
                return
        self.catalogo.append(l1)
        
    def rimuovi_libro(self, l1):
        
        for libro in self.catalogo:
            if libro.isbn == l1.isbn:
                self.catalogo.remove(l1)
                print("Il libro è stato rimosso.")
                return
        print("Libro non presente.")
        
        
    def cerca_per_titolo(self, l1):
        new_list = []
        for libro in self.catalogo:
            if libro.titolo == l1.titolo:
                new_list.append(libro)
                print("Il libro è stato salvato.")
                return new_list
            
        print("Libro non presente!")
        
    def mostra_catalogo(self):
        
        for libro in self.catalogo:
            
            libro.descrizione()
        
        
    
        
    
        
        
        