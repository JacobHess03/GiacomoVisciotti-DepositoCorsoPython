   #Esercizio numero 3
accounts = [["admin", "12345"]]   # Lista di account, ognuno è [nome, password]

    #Punto 1
nome = input ("Inserisci il tuo nome: ")
password = input("Inserisci la tua password: ")
account1 = [nome, password]

    #Punto 2: Verifica credenziali
if account1 in accounts:
    print("Nome utente e password inseriti sono corretti, benvenuto!")
    scelta = input("Vuoi cambiare un dato? (s/n)")
    if scelta.lower() == 's':
        
        #Domanda segreta per cambio dato
        seleziona = input("Qual è il tuo cantante preferito?")
        if(seleziona == "Pippo Baudo"):
            comando  = input("Quale dato vuoi modificare? Nome o Password?")
            
            #Match per cambio dato
            match comando:
                case "Nome":
                    nome = input("Inserisci nuovo nome: ")
                    account1 = [nome, password]
                case "Password":
                    password = input("Inserisci nuova password: ")
                    account1 = [nome, password]

        else:
            
            #Controllo sulla risposta
            print("Risposta non corretta!")           
        
else:
    print("Nome utente e password inseriti non sono corretti")
    
    #Stampa di verifica
print(account1)

