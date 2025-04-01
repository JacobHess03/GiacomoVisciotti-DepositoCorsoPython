import random
seleziona = int(input("Quale esercizio vuoi eseguiure? 1. ,2. ,3., 4., 5., 6., 7."))

match seleziona:
    case 1:
            #inserimento del numero
        num = int(input("Inserisci il numero: "))
        numeri = []
        somma = 0
        flag = True
        while(flag):
            
            numeri.append(num)
            if num > 0:
                flag = False
            else:
                num = int(input("Inserisci il numero: "))

        for i in numeri:
            somma = somma + i

        print(somma)
    
    case 2:
        num = int(input("Inserisci il numero: "))
            #inizializzo la lista
        lista_casuale = []  

        for i in range(num):  
            lista_casuale.append(random.randint(1, num))  
            #uso lo splat per spacchettare la lista
        lista_casuale = [*lista_casuale]  

        print(lista_casuale)

    case 3:
        flag = True
        numeri = []
        while(flag):
            x = int("Inserisci un numero nella lista")
            numeri.append(x)
            scelta = input("Vuoi con inserire un altro numero? (s/n)")
            if scelta.lower() == "no":
                flag = False
            # inizializzo la somma stampo la somma che restituise un numero pari
        somma_pari = 0  

        for numero in numeri:
            if numero % 2 == 0:
                somma_pari += numero

        print(somma_pari)
    
    case 4:
        flag = True
        numeri = []
        while(flag):
            x = int(input("Inserisci un numero nella lista: "))
            numeri.append(x)
            scelta = input("Vuoi inserire ancora? (s/n)")
            if scelta.lower() == "no":
                flag = False
        
        for numero in numeri:
            if numero % 2 != 0:
                print(numero)
    case 5:
            #definisco la funzione per verificare se il numero è primo
        def is_primo(n):
            if n < 2:
                    return False
            for i in range(2, n + 1):
                if n % i == 0:
                    return False
            return True
        
        flag = True
        numeri = []
        while(flag):
            x = int(input("Inserisci un numero nella lista: "))
            numeri.append(x)
            scelta = input("Vuoi inserire ancora? (s/n)")
            if scelta.lower() == "no":
                flag = False
            #stampo se il numero è primo o meno
        for numero in numeri:
            print(is_primo(numero))
                
    
    
    case 6:
    
        
        def is_primo(n):
            if n < 2:
                    return False
            for i in range(2, n + 1):
                if n % i == 0:
                    return False
            return True
        
        flag = True
        numeri = []
        while(flag):
            x = int(input("Inserisci un numero nella lista: "))
            numeri.append(x)
            scelta = input("Vuoi inserire ancora? (s/n)")
            if scelta.lower() == "no":
                flag = False
        
        for numero in numeri:
            if is_primo(numero):
                    #stampo il numero primo dopo averlo verificato
                print(numero)
    
    case 7:
            
        
        def is_primo(n):
            if n < 2:
                    return False
            for i in range(2, n + 1):
                if n % i == 0:
                    return False
            return True
        
        flag = True
        numeri = []
        while(flag):
            x = int(input("Inserisci un numero nella lista: "))
            numeri.append(x)
            scelta = input("Vuoi inserire ancora? (s/n)")
            if scelta.lower() == "no":
                flag = False
        
        for numero in numeri:
            if is_primo(numero):
                numero_primo = numero_primo + numero
                #se la somma è numero primo la stampo altrimenti messaggio di avviso
        if is_primo(numero_primo):
            print("La somma è un numero primo: ", numero_primo)
        else:
            print("La somma non è un numero primo")
            
        
        

        
        
