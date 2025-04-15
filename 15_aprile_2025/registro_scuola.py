# Classe base Persona
class Persona:
    def __init__(self, nome, eta):
        self.__nome = None
        self.__eta = None
        self.set_nome(nome)
        self.set_eta(eta)

    # Getter e Setter per nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if type(nome) == str and nome.strip():
            self.__nome = nome.strip()
        else:
            raise ValueError("Il nome deve essere una stringa non vuota.")

    # Getter e Setter per età
    def get_eta(self):
        return self.__eta

    def set_eta(self, eta):
        try:
            eta = int(eta)
            if eta >= 0:
                self.__eta = eta
            else:
                raise ValueError
        except:
            raise ValueError("L'età deve essere un numero intero non negativo.")

    # Metodo presentazione (base)
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.__nome} e ho {self.__eta} anni.")


# Sottoclasse Studente
class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.voti = voti if type(voti) == list else []

    def __calcola_media(self):
        if self.voti:
            return sum(self.voti) / len(self.voti)
        return 0.0

    # Override del metodo presentazione
    def presentazione(self):
        media = self.__calcola_media()
        super().presentazione()
        print(f"La mia media voti è {media:.2f}.")


# Sottoclasse Professore
class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia if type(materia) == str else "Materia non specificata"

    # Override del metodo presentazione
    def presentazione(self):
        super().presentazione()
        print(f"Insegno {self.__materia}.")
        

class Scuola:
    def __init__(self, nome):
        self.__nome = nome
        self.__studenti = []
        self.__professori = []

    def aggiungi_studente(self):
        voti = []
        nome = input("Inserisci un nome per lo studente: ").strip()
        eta = int(input("Inserisci l'età dello studente: "))
        
        while True:
            voto = int(input("Inserisci il voto: "))
            voti.append(voto)
            scelta = input("Vuoi inserire un altro voto? (s/n)")
            if scelta.lower() == "no":
                break
        studente = Studente(nome, eta, voti)
        if isinstance(studente, Studente):
            self.__studenti.append(studente)
        else:
            raise TypeError("Solo oggetti di tipo Studente possono essere aggiunti.")

    def aggiungi_professore(self):
        nome = input("Inserisci un nome per il professore: ").strip()
        eta = int(input("Inserisci l'età del professore: "))
        materia = input("Inserisci la materia: ").strip()
        professore = Professore(nome, eta, materia)
        if isinstance(professore, Professore):
            self.__professori.append(professore)
        else:
            raise TypeError("Solo oggetti di tipo Professore possono essere aggiunti.")

    def mostra_studenti(self):
        if not self.__studenti:
            print("Nessuno studente registrato.")
        for s in self.__studenti:
            s.presentazione()

    def mostra_professori(self):
        if not self.__professori:
            print("Nessun professore registrato.")
        for p in self.__professori:
            p.presentazione()

    def cerca_persona(self, nome):
        trovati = []

        for persona in self.__studenti + self.__professori:
            if persona.get_nome().lower() == nome.lower():
                trovati.append(persona)

        if trovati:
            print(f"\nTrovati {len(trovati)} risultati per '{nome}':")
            for persona in trovati:
                persona.presentazione()
        else:
            print(f"Nessuna persona trovata con il nome '{nome}'.")
    
    
def menu_principale():
    scuola = Scuola("Istituto Tecnico Superiore")

    while True:
        print("\n=== MENU SCUOLA ===")
        print("1. Aggiungi Studente")
        print("2. Aggiungi Professore")
        print("3. Mostra Studenti")
        print("4. Mostra Professori")
        print("5. Cerca Persona per Nome")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ").strip()

        match scelta:
            case "1":
                try:
                    scuola.aggiungi_studente()
                except Exception as e:
                    print("Errore:", e)

            case "2":
                try:
                    scuola.aggiungi_professore()
                except Exception as e:
                    print("Errore:", e)

            case "3":
                scuola.mostra_studenti()

            case "4":
                scuola.mostra_professori()

            case "5":
                nome = input("Inserisci il nome della persona da cercare: ").strip()
                scuola.cerca_persona(nome)

            case "0":
                print("Uscita dal programma.")
                break

            case _:
                print("Opzione non valida. Riprova.")


# Avvio del programma
if __name__ == "__main__":
    menu_principale()



