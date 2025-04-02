# Liste globali per tracciare corsi e utenti
corsi = {"Pilates": [], "Sala Pesi": [], "Ginnastica Posturale": []}
utenti = []  # Lista per rappresentare gli utenti
id_utenti = []  # Lista per tracciare gli ID degli utenti

# Decoratore per controllare l'inserimento di nome e cognome (Decoratore di esempio!)
def controllo_inserimento(funzione):
    def wrapper():
        valore = funzione()
        if valore == "":  # Controlla se il valore è vuoto o solo spazi
            print("Input non valido, riprova.")
            return wrapper()  # Richiama la funzione per un nuovo input
        return valore
    return wrapper

@controllo_inserimento
def inserisci_nome():
    # Funzione per inserire un nome
    return input("Inserisci il tuo nome: ")

@controllo_inserimento
def inserisci_cognome():
    # Funzione per inserire un cognome
    return input("Inserisci il tuo cognome: ")

# Metodo per creare un utente
def crea_utente(utenti, id_utenti, nome, cognome):
    # Controllo se l'utente esiste già
    for utente in utenti:
        if utente["nome"] == nome and utente["cognome"] == cognome:
            print("Utente già esistente")
            return False

    # Creazione del nuovo utente
    id_utente = len(id_utenti) + 1
    nuovo_utente = {"id": id_utente, "nome": nome, "cognome": cognome, "corsi_iscritti": 0}
    utenti.append(nuovo_utente)
    id_utenti.append(id_utente)

    print("Utente creato con successo")
    print(f"ID utente assegnato: {id_utente}")
    return True


# Metodo per iscrivere un utente a un corso
def iscrivi_corso(corsi, utenti, nome, cognome, corso):
    # Controllo se il corso esiste
    if corso not in corsi:
        print("Corso non valido")
        return False

    # Controllo se l'utente esiste
    for utente in utenti:
        if utente["nome"] == nome and utente["cognome"] == cognome:
            # Controllo se l'utente ha già raggiunto il limite di 2 corsi
            if utente["corsi_iscritti"] >= 2:
                print("Hai già raggiunto il limite massimo di 2 corsi.")
                return False

            # Controllo se il corso ha raggiunto il limite di 10 iscritti
            if len(corsi[corso]) >= 10:
                print(f"Il corso {corso} ha raggiunto il limite massimo di 10 iscritti.")
                return False

            # Iscrizione al corso
            corsi[corso].append(utente["id"])
            utente["corsi_iscritti"] += 1
            print(f"Iscrizione al corso {corso} avvenuta con successo")
            return True

    print("Utente non trovato")
    return False


# Metodo per visualizzare lo stato dei corsi
def visualizza_corsi(corsi, utenti):
    for corso in corsi:
        iscritti = corsi[corso]
        print(f"Corso: {corso} - Iscritti: {len(iscritti)}/10")
        for id_utente in iscritti:
            for utente in utenti:
                if utente["id"] == id_utente:
                    print(f"  - {utente['nome']} {utente['cognome']} (ID: {utente['id']})")
                    break


# Ciclo principale
flag = True
while flag:
    scelta = int(input("Ciao, inserisci la scelta\n1. Registrati\n2. Iscriviti a un corso\n3. Visualizza corsi\n4. Esci\n"))

    match scelta:
        case 1:
            nome = inserisci_nome()
            cognome = inserisci_cognome()
            crea_utente(utenti, id_utenti, nome, cognome)

        case 2:
            nome = input("Inserire nome: ")
            cognome = input("Inserire cognome: ")
            corso = input("Inserire il corso (Pilates, Sala Pesi, Ginnastica Posturale): ")
            iscrivi_corso(corsi, utenti, nome, cognome, corso)

        case 3:
            visualizza_corsi(corsi, utenti)

        case 4:
            print("Uscita dal programma")
            flag = False
