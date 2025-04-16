from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self._nome = nome
        self._cognome = cognome
        self._stipendio_base = stipendio_base
        
    # posso farli astratti
    def get_nome(self):
        return self._nome

    def get_cognome(self):
        return self._cognome

    @abstractmethod
    def calcola_stipendio(self):
        pass

    @abstractmethod
    def descrizione(self):
        pass


class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def get_nome(self):
        return super().get_nome()
    
    def get_cognome(self):
        return super().get_cognome()
    
    def calcola_stipendio(self):
        return self._stipendio_base

    def descrizione(self):
        print(f"[Fisso] {self._nome} {self._cognome} - Stipendio base: {self._stipendio_base}€")


class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
        self._vendite = []
        
    
    def get_nome(self):
        return super().get_nome()
    
    def get_cognome(self):
        return super().get_cognome()

    def aggiungi_vendita(self, importo):
        if importo > 0:
            self._vendite.append(importo)

    def calcola_stipendio(self):
        return self._stipendio_base + sum(self._vendite)

    def descrizione(self):
        print(f"[A Provvigione] {self._nome} {self._cognome} - Base: {self._stipendio_base}€ - Vendite: {self._vendite}")


class GestoreImpiegati:
    def __init__(self):
        self.impiegati = []

    def aggiungi_impiegato_fisso(self, nome, cognome, stipendio_base):
        impiegato = ImpiegatoFisso(nome, cognome, stipendio_base)
        self.impiegati.append(impiegato)

    def aggiungi_impiegato_provvigione(self, nome, cognome, stipendio_base):
        impiegato = ImpiegatoAProvvigione(nome, cognome, stipendio_base)
        self.impiegati.append(impiegato)

    def aggiungi_vendita(self, nome, cognome, importo):
        for imp in self.impiegati:
            if imp.get_nome() == nome and imp.get_cognome() == cognome:
                if isinstance(imp, ImpiegatoAProvvigione):
                    imp.aggiungi_vendita(importo)
                    print(f"Vendita di {importo}€ aggiunta a {nome} {cognome}")
                    return
                else:
                    print(f"{nome} {cognome} non è un impiegato a provvigione.")
                    return
        print(f"Impiegato {nome} {cognome} non trovato.")

    def mostra_stipendi(self):
        for imp in self.impiegati:
            print(f"{imp.get_nome()} {imp.get_cognome()} - Stipendio totale: {imp.calcola_stipendio()}€")

    def mostra_descrizioni(self):
        for imp in self.impiegati:
            imp.descrizione()

class Admin:
    def __init__(self, username, password, nome, email, ruolo="Amministratore"):
        self.__username = username
        self.__password = password
        self.__nome = nome
        self.__email = email
        self.__ruolo = ruolo
        self.__logged_in = False

    def login(self, username, password):
        if self.__username == username and self.__password == password:
            self.__logged_in = True
            print(f"Accesso effettuato! Benvenuto, {self.__nome}.")
        else:
            print("Credenziali non valide.")

    def logout(self):
        self.__logged_in = False
        print("Disconnessione avvenuta con successo.")

    def is_logged_in(self):
        return self.__logged_in

    def mostra_dati_personali(self):
        if self.__logged_in:
            print("=== DATI ADMIN ===")
            print(f"Nome: {self.__nome}")
            print(f"Email: {self.__email}")
            print(f"Ruolo: {self.__ruolo}")
            print("==================")
        else:
            print("Devi effettuare il login per visualizzare i dati personali.")


def menu():
    admin = Admin("admin", "1234", "Giacomo Visciotti", "giacomo@azienda.com")
    gestore = GestoreImpiegati()

    while True:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Login Admin")
        print("2. Visualizza dati Admin")
        print("3. Aggiungi Impiegato Fisso")
        print("4. Aggiungi Impiegato a Provvigione")
        print("5. Aggiungi Vendita a Impiegato")
        print("6. Mostra Descrizioni Impiegati")
        print("7. Mostra Stipendi Impiegati")
        print("8. Logout Admin")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            username = input("Username: ")
            password = input("Password: ")
            admin.login(username, password)

        elif scelta == "2":
            admin.mostra_dati_personali()

        elif scelta == "3":
            if admin.is_logged_in():
                nome = input("Nome: ")
                cognome = input("Cognome: ")
                stipendio = float(input("Stipendio base: "))
                gestore.aggiungi_impiegato_fisso(nome, cognome, stipendio)
            else:
                print("Devi effettuare il login come admin.")

        elif scelta == "4":
            if admin.is_logged_in():
                nome = input("Nome: ")
                cognome = input("Cognome: ")
                stipendio = float(input("Stipendio base: "))
                gestore.aggiungi_impiegato_provvigione(nome, cognome, stipendio)
            else:
                print("Devi effettuare il login come admin.")

        elif scelta == "5":
            if admin.is_logged_in():
                nome = input("Nome: ")
                cognome = input("Cognome: ")
                importo = float(input("Importo vendita: "))
                gestore.aggiungi_vendita(nome, cognome, importo)
            else:
                print("Devi effettuare il login come admin.")

        elif scelta == "6":
            gestore.mostra_descrizioni()

        elif scelta == "7":
            gestore.mostra_stipendi()

        elif scelta == "8":
            admin.logout()

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida. Riprova.")
            
            
menu()
