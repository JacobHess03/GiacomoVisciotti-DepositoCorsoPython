import random

def genera_numero():
        #genero un numero casuale
    return random.randint(1, 100)

def ottieni_tentativo():
     #chiedo all'utente di inserire un numero o di uscire dal gioco
    while True:
        num = input("Inserisci un numero tra 1 e 100 o 'esci' per terminare: ")
        if num.lower() == 'esci':
            break
        else:
            numero = num
            if 1 <= numero <= 100:
                return numero
            else:
                print("Numero fuori intervallo, inserisci un valore tra 1 e 100.")

def verifica_tentativo(numero_da_indovinare, tentativo):
    #confronto il numero inserito con quello da indovinare e fornisce un suggerimento
    if tentativo < numero_da_indovinare:
        print("Troppo basso")
    elif tentativo > numero_da_indovinare:
        print("Troppo alto")
    else:
        print("Hai indovinato il numero")

def gioco_indovina_numero():
    #funzione principale che gestisce il gioco
    numero_da_indovinare = genera_numero()
    
    while True:
        tentativo = ottieni_tentativo()
        if tentativo is None:
            print("Il numero da indovinare era", numero_da_indovinare)
            break
        
        verifica_tentativo(numero_da_indovinare, tentativo)
        
        if tentativo == numero_da_indovinare:
            break

# avvio il gioco
gioco_indovina_numero()
