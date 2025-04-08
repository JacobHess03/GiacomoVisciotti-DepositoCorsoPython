def cifra(testo, chiave):
    # Crea un dizionario inverso, mappando le lettere ai numeri
    alfabeto_chiave_lettera = {v: k for k, v in alfabeto_chiave_id.items()}
    
    # Cifratura
    testo_cifrato = []
    
    for char in testo:
        if char in alfabeto_chiave_lettera:
            # Trova la posizione numerica del carattere nel dizionario
            posizione = alfabeto_chiave_lettera[char]
            
            # Applica la chiave con il modulo 126 (per includere anche caratteri speciali)
            nuova_posizione = (posizione + chiave) % 126
            
            # Trova il carattere corrispondente alla nuova posizione
            testo_cifrato.append(alfabeto_chiave_id[nuova_posizione])
        else:
             # Se non lo trova space lo appende
            testo_cifrato.append(char)

    
    return ''.join(testo_cifrato) #per restituire una stringa


def decifra(testo, chiave):
    return cifra(testo, -chiave)


# Dizionario di mappatura
alfabeto_chiave_id = {
    # Numeri -> Lettere maiuscole (1-26)
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
    10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
    18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
    26: 'Z',
    
    # Numeri -> Lettere minuscole (101-126)
    101: 'a', 102: 'b', 103: 'c', 104: 'd', 105: 'e', 106: 'f', 107: 'g',
    108: 'h', 109: 'i', 110: 'j', 111: 'k', 112: 'l', 113: 'm', 114: 'n',
    115: 'o', 116: 'p', 117: 'q', 118: 'r', 119: 's', 120: 't', 121: 'u',
    122: 'v', 123: 'w', 124: 'x', 125: 'y', 126: 'z',
}

# Chiedi all'utente quale operazione vuole fare
operazione = input("Scegli operazione (cifra/decifra): ").lower()
frase = input("Inserisci la frase o la parola: ").strip()  
chiave = int(input("Inserisci la chiave (numero): ").strip())

# Esegui l'operazione
if operazione == "cifra":
    print(f"Parola cifrata: {cifra(frase, chiave)}")
elif operazione == "decifra":
    print(f"Parola decifrata: {decifra(frase, chiave)}")
else:
    print("Operazione non valida.")
