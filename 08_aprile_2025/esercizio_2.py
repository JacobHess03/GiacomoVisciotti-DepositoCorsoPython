# Restituire parole duplicate a partire dagli articoli (quindi >= 2)
def pulisciParola(ins):
    sostpromax = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 
    '{', '|', '}', '~', '£', '€', '¥', '§', '©', '®', '™', '°', '±', '¶', '•',
    '–', '—', '‘', '’', '“', '”', '„', '…', '‰', '‹', '›', '⁄', '⁎', '⁑', '⁓',
    '₤', '₧', '₨', '₩', '₪', '₫', '€', '₭', '₮', '₯', '₰', '₱', '₲', '₳', '₴',
    '₵', '₶', '₷', '₸', '₹', '₺', '₻', '₼', '₽', '₾', '₿']
    for c in sostpromax: # ciclo tutti i careatteri speciali e tramite replace sostituiamo con il nulla
        ins = ins.replace(c,"")
    return ins


def contaParole(inserimento): # Funzione che controlla i duplicati
    conteggio = {}
    parole = inserimento.split()
    for parola in parole:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

    duplicato = {k : v for k,v in conteggio.items() if v > 1}
    #non inline
    duplicato = {}
    for k, v in conteggio.items():
        if v > 1:
            duplicato[k] = v
     
    for key, value in duplicato.items():
        print(f"\nLa parola [{key}] appare [{value}] volte, ed è lunga [{len(key)}]!")
        
    if not duplicato:
        print("Non ci sono duplicati.\n")
    
    

inserimento = input("\nBenvenuto in Duplicas!\nInserisci la tua parola o frase: ").lower()
ins = pulisciParola(inserimento)
contaParole(ins)