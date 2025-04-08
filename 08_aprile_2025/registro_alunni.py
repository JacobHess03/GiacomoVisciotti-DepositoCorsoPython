

def calcola_media(voti):
    somma = 0
    for voto in voti:
        somma += voto
    return round(somma / len(voti), 2)

def crea_file_csv():
    try:
        # Se il file non esiste, lo crea con intestazione
        with open("08_aprile_2025\\registro.csv", "w") as file:
            file.write("Nome,Cognome,Voti,Media") # costruisce il csv 1 riga
    except:
        pass  # Se il file esiste, non fa nulla

def aggiungi_alunno():
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    numero_voti = int(input("Quanti voti vuoi inserire? "))
    
    voti = []
    for i in range(numero_voti):
        voto = int(input(f"Inserisci voto {i+1}: "))
        voti.append(voto)
    
    voti_str = "-".join([str(v) for v in voti]) # list comprension
    
    # # Trasformazione manuale in stringa separata da virgole
    # voti_str = ""
    # for i in range(len(voti)):
    #     voti_str += str(voti[i])
    #     if i < len(voti) - 1:
    #         voti_str += ","  # aggiunge la virgola solo se non è l'ultimo voto

        
       
    media = calcola_media(voti)
    
   
    
    with open("08_aprile_2025\\registro.csv", "a") as file:
        file.write(f"\n{nome},{cognome},{voti_str},{media}") #Giacomo, Visciotti, 1-2-3-4, media riga 2
    print("Alunno aggiunto!\n")

def mostra_alunni():
    try:
        with open("08_aprile_2025\\registro.csv", "r") as file:
            righe = file.read()
        righe_lista = righe.split("\n")
        if len(righe_lista) <= 1:
            print("Nessun alunno nel registro.\n")
        else:
            print("\n--- Registro Alunni ---")
            for riga in righe_lista: 
                print(riga.strip())
    except:
        print("Errore nella lettura del file.")

def modifica_alunno():
    nome = input("Nome dell'alunno da modificare: ").strip()
    cognome = input("Cognome: ").strip()
    trovato = False
    nuove_righe = []

    with open("08_aprile_2025\\registro.csv", "r") as file:
        contenuto = file.read()
    
    righe = contenuto.splitlines()  # ottengo una lista di righe oppure split(\n)

    for riga in righe:
        dati = riga.strip().split(",")  # esempio: Giacomo,Visciotti,7-8-9,8.0
        
        if dati[0] == nome and dati[1] == cognome:
            trovato = True
            print("Alunno trovato. Inserisci i nuovi voti.")
            nuovi_voti = []
            numero = int(input("Quanti voti vuoi inserire? "))
            for i in range(numero):
                voto = int(input(f"Voto {i+1}: "))
                nuovi_voti.append(voto)
            media = calcola_media(nuovi_voti)
            voti_str = "-".join(str(v) for v in nuovi_voti)
            nuove_righe.append(f"{nome},{cognome},{voti_str},{media}") # appendo stringhe, lista di stringhe posso fare il join
        else:
            nuove_righe.append(riga)  # mantieni le righe non modificate
    if trovato:
        with open("08_aprile_2025\\registro.csv", "w") as file:
            file.write("\n".join(nuove_righe))  # Unisce tutte le righe con "\n"
        print("Alunno modificato!\n")
    else:
        print("Alunno non trovato.\n")




# Programma principale
crea_file_csv()

while True:
    print("\n--- MENU ---")
    print("1. Aggiungi alunno")
    print("2. Mostra registro")
    print("3. Modifica alunno")
    print("4. Esci")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        aggiungi_alunno()
    elif scelta == "2":
        mostra_alunni()
    elif scelta == "3":
        modifica_alunno()
    elif scelta == "4":
        print("Uscita...")
        break
    else:
        print("Scelta non valida.\n")
