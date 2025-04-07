def conta_chiavi(stringa):
    #parola = stringa.split() con le parole 
    dizionario = {}
    for carattere in stringa:
        if carattere in dizionario:
            dizionario[carattere] += 1 #assegnazione del valore in base alla chiave
        else:
            dizionario[carattere] = 1
    return dizionario


stringa = input("Inserisci una stringa: ")
dizionario = conta_chiavi(stringa)
print(dizionario)

