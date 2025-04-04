# Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che pruce
# e vende vari tipi di prodotti. Gli studenti dovranno creare una classe chiamata
# Prodotto e diverse classi parallele che rappresentano i diversi tipi di prodotti
# Inoltre, dovranno creare una classe chiamata Fabbrica che gestisce l'invenatario e le
# vendite dei prodotti.

# 1. Creare una classe Prodotto con i seguenti attributi
# Classe Prodotto
class Prodotto:
    quantità = 0  # Quantità del prodotto
    # Attributi di classe
    nome = ""  # Nome del prodotto
    costo_produzione = 0.0  # Costo del prodotto
    prezzo_vendita = 0.0  # Prezzo del prodotto
    
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        # Inizializza le proprietà del prodotto
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
     
   
   
        
    def calcola_profitto(self):
        # Calcola il profitto del prodotto
        return self.prezzo_vendita - self.costo_produzione
    
   
# 3. Classe Fabbrica:
class Fabbrica:
    # Attributi di classe
    inventario = []  # Lista di prodotti in inventario
    
    def __init__(self, nome_fabbrica):
        # Inizializza il nome della fabbrica
        self.nome_fabbrica = nome_fabbrica
       
        
    def aggiungi_prodotto(self, Prodotto):
        
        if(Prodotto in self.inventario):
            # incrementa la quantità del prodotto
            Prodotto.quantità += 1
        else:
            # inizializza la quantità del prodotto
            Prodotto.quantità = 1
            # Aggiunge un prodotto all'inventario
            self.inventario.append(Prodotto)
        
    #classic method per cacolore il profitto
    
    @classmethod
    def calcola_profitto_totale(cls):
        # Calcola il profitto totale dell'inventario
        profitto_totale = 0.0
        for prodotto in cls.inventario:
            profitto_totale += prodotto.calcola_profitto()
        return profitto_totale
   
        
    def vendi_prodotto(self, nome_prodotto):
        # inserisco la quantità del prodotto da vendere
        quantità = int(input("Inserisci la quantità da vendere: "))
        # Vende un prodotto specifico e lo rimuove dall'inventario e stampa il profitto
        for prodotto in self.inventario:
            if prodotto.nome == nome_prodotto and prodotto.quantità >= quantità:
                prodotto.quantità -= quantità
                profitto = prodotto.calcola_profitto()
                print(f"Prodotto venduto: {prodotto.nome}, Profitto: {profitto}, Profitto totale: {self.calcola_profitto_totale()}")
                return prodotto
        return None

    def resi_prodotto(self, nome_prodotto):
        # Passo il prodotto da restituire come class Prodotto
        for prodotto in self.inventario:
            if prodotto.nome == nome_prodotto:
                prodotto.quantità += 1
                print("Prodotto restituito con successo.")
                return True
        print("Prodotto non trovato nell'inventario.")
        return False
    
    
# creo la fabbrica
f1 = Fabbrica("Fabbrica di Elettronica")
flag = True

while flag:
    print("1. Aggiungi prodotto")
    print("2. Vendi prodotto")
    print("3. Restituisci prodotto")
    print("4. Calcola profitto totale")
    print("5. Esci")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        
        nome_prodotto = input("Inserisci il nome del prodotto: ")
        costo_produzione = float(input("Inserisci il costo di produzione: "))
        prezzo_vendita = float(input("Inserisci il prezzo di vendita: "))
        p1 = Prodotto(nome_prodotto, costo_produzione, prezzo_vendita)
        f1.aggiungi_prodotto(p1)
    elif scelta == "2":
        nome_prodotto = input("Inserisci il nome del prodotto da vendere: ")
        f1.vendi_prodotto(nome_prodotto)
    elif scelta == "3":
        nome_prodotto = input("Inserisci il nome del prodotto da restituire: ")
        f1.resi_prodotto(nome_prodotto)
    elif scelta == "4":
        print(f"Profitto totale dell'inventario: {f1.calcola_profitto_totale()}")
    elif scelta == "5":
        flag = False
    else:
        print("Opzione non valida.")


