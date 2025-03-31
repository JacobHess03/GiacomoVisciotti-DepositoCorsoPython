    #Menù di selezione esercizi
seleziona = int(input("Quale dei due esercizi vuoi vedere? 1., 2., 3.?"))
match seleziona:
    case 1:
            #Inserimento numero e conto alla rovescia
        bound = int(input("Inserisci un numero"))
        for i in range (bound, -1, -1):
            print(i)
    case 2:
        insieme = 0
        while (insieme < 5):
    
            num = int(input("Inserisci un numero: "))

                #Controllo con l'operatore resto se il numero è divisibile per 2
                #se è pari incremento la variabile insieme e salvo il numero
            if num % 2 == 0:
                numero_saved = num
                print("è numero pari.")
                
                insieme += 1
            
                
            else:
                print("Non è un numero pari.")
    case 3:
        insieme = 0
        while (insieme < 5):


            num = int(input("Inserisci un numero: "))
            #Controllo con l'operatore resto se il numero è divisibile per 2
            #se è pari incremento la variabile insieme e salvo il numero

            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        print("Non è un numero primo.")
                
                    else:
                        print("È un numero primo.")
                        numero_saved = num
                        insieme += 1
            else:
                    print("Non è un numero primo.")
    