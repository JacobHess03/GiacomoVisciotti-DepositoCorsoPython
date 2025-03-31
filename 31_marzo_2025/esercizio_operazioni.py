    #Esercizio 2
    #Inserimento primi 2 numeri
num_1 = int(input("Inserisci il primo numero: "))
num_2 = int(input("Inserisci il secondo numero: "))

    #Ipotizzando ci siano soltanto queste operazioni ed operazioni "multiple"
comando  = int(input("Quale operazione vuoi eseguire: 1.(+), 2.(-), 3.(*), 4.(/), 5.(+) & (-), 6.(*) & (/) "))
    #match case per il menù di selezione
match comando:
    #elenco di operazioni
    case 1 :
        print("Ecco il risultato", num_1 + num_2)
    case 2 :
        print("Ecco il risultato", num_1 - num_2)
    case 3 :
        print("Ecco il risultato", num_1 * num_2)
    case 4 :
        if(num_2 == 0):
            print("Impossibile dividere per zero!")
        else:
            print("Ecco il risultato", num_1/num_2)
    case 5:
        print("Ecco il risultato della prima operazione: ", num_1 + num_2 )
        print("Ecco il risultato della prima operazione: ", num_1 - num_2 )
        
    case 6:
        if(num_2 == 0):
            #Controllo dello zero per non eseguire l'operazione
            print("Ecco il risultato della prima operazione: ", num_1 * num_2 )
            print("Impossibile eseguire l'operazione di divisione")
        else:
            print("Ecco il risultato della prima operazione: ", num_1 * num_2 )
            print("Ecco il risultato della seconda operazione: ", num_1 / num_2 )

    case _:
        print("Comando non riconosciuto")
    