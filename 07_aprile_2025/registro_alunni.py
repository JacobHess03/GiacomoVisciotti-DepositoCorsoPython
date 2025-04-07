
def calcola_media(registro, chiave):
    
    if chiave in registro:
        voti = registro[chiave]["voti"]#Giacomo Visciotti -> voti 
        somma = 0
        for voto in voti: #scorre la lista
            somma = somma + voto
        media = somma / len(voti) #lunghezza lista di voti
        return media #ritorno al media alla funzione
    else:
        print("Alunno non presente.\n")

def aggiungi_alunno(registro):
    nome = input("Inserisci il nome dell'alunno: ")
    cognome = input("Inserisci il cognome dell'alunno: ")
    chiave = nome + " " + cognome

    print("Quanti voti vuoi inserire per ciascun alunno?")
    numero_voti = int(input("Numero di voti: "))

    voti = [] #lista vuota di voti
    
    for i in range(numero_voti):
        voto = int(input("Inserisci il voto numero: "))
        #voti.append({"Materia": materia, "voto": voti}) Aggiungendo un menu
        voti.append(voto)

    # registro[chiave] = voti #registro[Giacomo Visciotti]-> [6, 7, 8]]
    
    registro[chiave] = {"voti": voti} # dizionario nel dizionario un altro modo
    #registro[chiave]["voti"] = voti
    media = calcola_media(registro, chiave)
    registro[chiave]["media"] = round(media, 2) #aggiunta di round e media come chiave e valore media
    
    
    
    print("Alunno aggiunto.\n")






registro = {} #dizionario vuoto

while True:
    print("1. Aggiungi un nuovo alunno")
    print("2. Mostra il registro")
    print("3. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        aggiungi_alunno(registro)
    
    elif scelta == "2":
        print(registro) # mostra il registro 
        break
    elif scelta == "3":
        print("Uscita programma.")
        break
    else:
        print("Scelta non valida.\n")



