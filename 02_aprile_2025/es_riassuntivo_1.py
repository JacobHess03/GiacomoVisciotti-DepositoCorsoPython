
flag = True
while flag:
    #creazione menù scelta
    scelta = input("Scegli un argomento:\n1. Operazioni\n2. Variabili \n3. Liste \n4. Controllori di Flusso \n5. Tuple\n6. Insiemi\n7. Funzioni\n8. Decoratori\n9. Uscita\n")
    match scelta:
        case "1":
            # Operazioni
            print("Hai scelto Operazioni. Verrano stampate tramite il metodo print")
            # Assegnazione con casting
            print("Assegnazione con casting")
            a = int(input("Inserisci un numero: "))
            b = int(input("Inserisci un secondo numero: "))
            # Inserisci qui il codice per le operazioni
            #Addizione
            print(f"La somma di {a} e {b} è: {a + b}")
            # Sottrazione
            print(f"La differenza tra {a} e {b} è: {a - b}")
            # Moltiplicazione
            print(f"La moltiplicazione tra {a} e {b} è: {a * b}")
            # Divisione
            print(f"La divisione tra {a} e {b} è: {a / b}")
            # Il resto della divisione
            print(f"Il resto della divisione tra {a} e {b} è: {a % b}")
            # Potenza
            print(f"La potenza tra {a} e {b} è: {a ** b}")
        
        case "2":
            # Variabili basilari
            print("Hai scelto Variabili. Verrano stampate tramite il metodo print")
            a = int(input("Inserisci un numero: "))
            b = int(input("Inserisci un secondo numero: "))
            # Inserisci qui il codice per le variabili basilari
            print(f"Il valore di a è: {a}")
            print(f"Il valore di b è: {b}")
            #Variabili booleane
            c = True
            d = False
            print(f"Il valore di c è: {c}")
            print(f"Il valore di d è: {d}")
            #Variabili stringa non basilari
            e = "Ciao"
            f = "Mondo"
            print(f"La stringa e è: {e}")
            print(f"la stringa f è: {f}")
            
        case "3":
            # Liste
            print("Hai scelto Liste. Verrano stampate tramite il metodo print")
            # Inserisci qui il codice per le liste
            lista = [1, 2, 3, 4, 5]
            print(f"La lista è: {lista}")
            # Aggiungi un elemento alla lista
            lista.append(6)
            print(f"La lista dopo l'aggiunta è: {lista}")
            # Rimuovi un elemento dalla lista
            lista.remove(3)
            print(f"La lista dopo la rimozione è: {lista}")
            # Stampa il numero di elementi nella lista
            print(f"Il numero di elementi nella lista è: {len(lista)}")
            # Stampa il primo elemento della lista
            print(f"Il primo elemento della lista è: {lista[0]}")  
            # Reverse della lista
            lista.reverse()
            print(f"La lista dopo il reverse è: {lista}")
            # Ordinamento della lista
            lista.sort()
            print(f"La lista dopo l'ordinamento è: {lista}")
        
        case "4":
            # Controllori di Flusso
            print("Hai scelto Controllori di Flusso. Verrano stampate tramite il metodo print")
            a = int(input("Inserisci un numero: "))
            # Inserisci qui il codice per i controllori di flusso
            # If-else
            print("Controllo if-else")
            if a > 0:
                print(f"{a} è positivo")
            elif a < 0:
                print(f"{a} è negativo")
            else:
                print(f"{a} è zero")
            
            # Ciclo for matematico
            print("Ciclo for matematico")
            for i in range(5):
                print(f"Iterazione {i}")

            #Ciclo for con lista
            lista = ["Ciro", "Mirko", 3, 4, 5] 
            print("Ciclo for con lista")
            for i in lista:
                print(f"Elemento {i}")
                
            # Ciclo while a condizione
            print("Ciclo while a condizione")
            i = 0 
            while i < 5:
                print(f"Iterazione {i}")
                i += 1
        
        case "5":
            # Tuple
            print("Hai scelto Tuple. Verrano stampate tramite il metodo print")
            # Inserisci qui il codice per le tuple
            tupla = (1, 2, 3, 4, 5)
            print(f"La tupla è: {tupla}")
            # Stampa il primo elemento della tupla
            print(f"Il primo elemento della tupla è: {tupla[0]}")
            # Stampa il numero di elementi nella tupla
            print(f"Il numero di elementi nella tupla è: {len(tupla)}")
            # Unpacking della tupla
            a, b, c, d, e = tupla
            print(f"I valori unpacked sono: {a}, {b}, {c}, {d}, {e}")
        
        case "6":
            # Insiemi
            print("Hai scelto Insiemi. Verrano stampate tramite il metodo print")
            # Inserisci qui il codice per gli insiemi
            insieme1 = {1, 2, 3, 4, 5}
            insieme2 = {4, 5, 6, 7, 8}
            print(f"L'insieme1 è: {insieme1}")
            print(f"L'insieme2 è: {insieme2}")
            # Unione degli insiemi
            unione = insieme1.union(insieme2)
            print(f"L'unione degli insiemi è: {unione}")
            # Intersezione degli insiemi
            intersezione = insieme1.intersection(insieme2)
            print(f"L'intersezione degli insiemi è: {intersezione}")
            # Differenza tra gli insiemi
            differenza = insieme1.difference(insieme2)
            print(f"La differenza tra gli insiemi è: {differenza}")
            # Differenza simmetrica tra gli insiemi
            differenza_simmetrica = insieme1.symmetric_difference(insieme2)
            print(f"La differenza simmetrica tra gli insiemi è: {differenza_simmetrica}")
        
        case "7":
            # Funzioni
            print("Hai scelto Funzioni. Verrano stampate tramite il metodo print")
            
            # Funzioni di ritorno
            print("Funzioni di ritorno")
            def somma(a, b):
                return a + b
            
            def sottrazione(a, b):
                return a - b
            
            a = int(input("Inserisci un numero: "))
            b = int(input("Inserisci un secondo numero: "))
            
            print(f"La somma di {a} e {b} è: {somma(a, b)}")
            print(f"La sottrazione di {a} e {b} è: {sottrazione(a, b)}")
            
            # Funzioni senza ritorno
            print("Funzioni senza ritorno")
            def stampa_messaggio(messaggio):
                print(messaggio)
            stampa_messaggio("Ciao Ciro, è tutta colpa tua!")
            
        case "8":
            # Decoratori
            print("Hai scelto Decoratori. Verrano stampate tramite il metodo print")
            
            # Decoratore semplice
            def decoratore(funzione):
                def wrapper():
                    print("Prima di eseguire la funzione")
                    funzione()
                    print("Dopo aver eseguito la funzione")
                return wrapper
            
            @decoratore
            def saluta():
                print("Ciao!")
            
            saluta()
            # Decoratore con argomenti 
            def decoratore_con_argomenti(funzione):
                def wrapper(*args, **kwargs):
                    print("Prima di eseguire la funzione")
                    risultato = funzione(*args, **kwargs)
                    print("Dopo aver eseguito la funzione")
                    return risultato
                return wrapper
            @decoratore_con_argomenti
            def somma(a, b):
                return a + b
            print(f"Il risultato della somma è: {somma(3, 4)}")
            # Decoratore con argomenti e modifica del risultato
            def decoratore_modifica(funzione):
                def wrapper(*args, **kwargs):
                    risultato = funzione(*args, **kwargs)
                    risultato += 1  # Modifica il risultato aggiungendo 1
                    return risultato
                return wrapper
            @decoratore_modifica
            def quadrato(x):
                return x * x
            print(f"Il quadrato è: {quadrato(2)}")
        
        case "9":
            # Uscita
            flag = False
        
        
        
        
        
        
        
