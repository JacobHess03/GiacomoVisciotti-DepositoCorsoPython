class Automobile:
    numero_di_ruote = 4 # Attributo di classe
    
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)
    
Auto1 = Automobile("Fiat", "Panda") #auto1 è un'istanza della classe Automobile riferita a self
Auto2 = Automobile("Ford", "Fiesta")
Auto1.numero_di_ruote = 5 # Modifica l'attributo di istanza
Auto1.stampa_info()
Auto2.stampa_info()
print("Numero di ruote:", Auto1.numero_di_ruote) # Stampa 5

class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
# Creazione di un oggetto Persona
P = Persona("Pippo", 30)

print(P.nome)  # Stampa "Pippo"
print(P.età)   # Stampa 30

#metodo statico
class Calcolatrice:
    
    @staticmethod
    def somma(a, b):
        return a + b
#uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)
# Output:8

# metodo decorato
class Contatore:
    numero_istanze = 0 # Attributo di classe
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.mostra_numero_istanze} istanze.")

# Creazione di alcune istanze
C1 = Contatore()
C2 = Contatore()

Contatore.mostra_numero_istanze()
#Out put: Sono state create 2 istanze