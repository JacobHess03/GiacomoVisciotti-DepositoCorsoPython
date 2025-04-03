# Classe che rappresenta un Libro
class Libro:
    def __init__(self, titolo, autore, pagine):
        # Inizializza le proprietà del libro
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def stampa_libro(self):
        # Stampa le informazioni del libro
        print(f"Il libro ha come titolo '{self.titolo}', autore '{self.autore}', numero di pagine {self.pagine}")


# Classe Biblioteca che contiene una lista di libri
class Biblioteca:
    def __init__(self, catalogo):
        # Inizializza la lista di libri
        self.catalogo = catalogo

    def aggiungi_libro(self, libro):
        # Aggiunge un libro al catalogo
        self.catalogo.append(libro)

    def stampa_catalogo(self):
        # Stampa l'elenco dei libri nel catalogo
        for libro in self.catalogo:
            libro.stampa_libro()


# Funzione per inserire libri nella biblioteca
def inserimento(biblioteca):
    continua = True
    while continua:
        # Richiede i dettagli del libro all'utente
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        pagine = int(input("Inserisci il numero di pagine: "))
        libro = Libro(titolo, autore, pagine)
        biblioteca.aggiungi_libro(libro)

        # Chiede se continuare l'inserimento
        risposta = input("Vuoi continuare a inserire? (NO per terminare): ")
        if risposta.upper() == "NO":
            continua = False


# Funzione per stampare i libri nella biblioteca
def stampa_catalogo(biblioteca):
    biblioteca.stampa_catalogo()


# Variabile per controllare il ciclo principale
flag = True

# Creazione della biblioteca
catalogo = []
biblioteca = Biblioteca(catalogo)

# Ciclo principale per gestire le operazioni
while flag:
    # Mostra il menu e richiede una scelta
    scelta = int(input("Inserisci cosa vuoi fare:\n1. Inserire Libro\n2. Stampare Catalogo\n3. Uscire\n"))

    match scelta:
        case 1:
            # Inserimento di un libro
            inserimento(biblioteca)
        case 2:
            # Stampa del catalogo
            stampa_catalogo(biblioteca)
        case 3:
            # Uscita dal programma
            print("Uscita programma...")
            flag = False
        case _:
            # Scelta non valida
            print("Scelta non valida, riprova.")
