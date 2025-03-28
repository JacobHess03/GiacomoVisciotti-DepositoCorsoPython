#Esercizio numero 1
#Inserisco il numero iniziale
risultato = int(input("Inserisci un numero: "))
#Verifico se è positivo
if(risultato > 0):
    risultato = int(input("Inserisci un numero: "))
    #Verifico se è maggiore di 10
    if (risultato > 10):
        risultato = int(input("Inserisci un numero: "))
        #verifico se è maggiore di 30
        if(risultato > 30):
            print("Ottimo! Sei arrivato alla fine")
            
        
#Esercizio numero 2
#Lista di nomi da gestire
nomi = ["Pippo", "Pluto", "Paperino"]
#Stampa dei nomi
print(nomi)
#Selezione di scelta 
seleziona = int(input("Seleziona la scelta: 1 Aggiungi, 2 Rimuovi, 3 Elimina"))
if (seleziona == 1):
    aggiunta = (input("Chi vuoi aggiungere: "))
    nomi.append(aggiunta)
elif(seleziona == 2):
    rimozione = (input("Chi vuoi rimuovere: ")) 
    nomi.remove(rimozione)
else:
    nomi.clear()
    
print(nomi)           


    #Esercizio numero 3
accounts = []   # Lista di account, ognuno è [id, nome, password]
next_id = 1     # Contatore per l'ID progressivo

scelta = input("Vuoi creare un nuovo account? (s/n): ")

if scelta.lower() == 's': #posso scrivere sia S che s
    # Creazione di un nuovo account
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")
    
    # Costruiamo la lista con i dati
    nuovo_account = [next_id, nome, password]
    accounts.append(nuovo_account)
    
    print(f"Account creato con successo! ID assegnato: {next_id}")
    next_id += 1

nome = input ("Inserisci il tuo nome: ")
password = input("Inserisci la tua password: ")
    #Controllo sul singolo account
if nome.lower() and password.lower() in nuovo_account:
    print("Account esistente")

    #Controllo sulla lista
if(nuovo_account in accounts):
    print("Account esistente")
else:
    print("Account non esistente")
            



        
    
        