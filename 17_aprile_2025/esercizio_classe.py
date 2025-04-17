import numpy as np

class ArraySpace:

    def __init__(self):
        self.array_1 = None
        self.array_2 = None

    def crea_array_equi(self, start, end, num):
        return np.linspace(start, end, num)

    def crea_array_casuale(self, num):
        return np.random.rand(num)

    def somma_array(self):
        if self.array_1 is not None and self.array_2 is not None:
            if self.array_1.shape == self.array_2.shape:
                return self.array_1 + self.array_2
            else:
                print("Errore: gli array non hanno la stessa lunghezza.")
                return None
        else:
            print("Errore: devi prima creare entrambi gli array.")
            return None

    def somma_totale(self):
        if self.array_1 is not None and self.array_2 is not None:
            if self.array_1.shape == self.array_2.shape:
                return np.sum(self.array_1) + np.sum(self.array_2)
            else:
                print("Errore: gli array non hanno la stessa lunghezza.")
                return None
        else:
            print("Errore: devi prima creare entrambi gli array.")
            return None

    def somma_maggiori_di_5(self):
        if self.array_1 is not None and self.array_2 is not None:
            somma_1 = np.sum(self.array_1[self.array_1 > 5])
            somma_2 = np.sum(self.array_2[self.array_2 > 5])
            return somma_1, somma_2
        else:
            print("Errore: devi prima creare entrambi gli array.")
            return None, None

    def stampa_dettagli(self):
        if self.array_1 is not None and self.array_2 is not None:
            if self.array_1.shape == self.array_2.shape:
                print("Array 1:\n", self.array_1)
                print("Array 2:\n", self.array_2)
                somma = self.array_1 + self.array_2
                print("Somma elemento per elemento:\n", somma)
                print(f"Somma totale Array 1: {np.sum(self.array_1):.3f}")
                print(f"Somma totale Array 2: {np.sum(self.array_2):.3f}")
                print(f"Somma totale combinata: {np.sum(somma):.3f}")
            else:
                print("Errore: gli array non hanno la stessa lunghezza.")
        else:
            print("Errore: devi prima creare entrambi gli array.")
            
def menu():
    spazio = ArraySpace()

    while True:
        print("\n--- MENU ---")
        print("1. Crea array 1 (equidistante)")
        print("2. Crea array 2 (casuale)")
        print("3. Somma i due array")
        print("4. Somma totale")
        print("5. Mostra array 1")
        print("6. Mostra array 2")
        print("7. Esci")
        print("8. Somma degli elementi > 5")
        print("9. Stampa dettagli completa")

        scelta = input("Seleziona un'opzione (1-9): ")

        match scelta:
            case "1":
                try:
                    start = float(input("Valore iniziale: "))
                    end = float(input("Valore finale: "))
                    num = int(input("Numero di elementi: "))
                    spazio.array_1 = spazio.crea_array_equi(start, end, num)
                    print("Array 1 creato!")
                except ValueError:
                    print("Input non valido. Riprova.")

            case "2":
                try:
                    num = int(input("Numero di elementi: "))
                    spazio.array_2 = spazio.crea_array_casuale(num)
                    print("Array 2 creato!")
                except ValueError:
                    print("Input non valido. Riprova.")

            case "3":
                somma = spazio.somma_array()
                if somma is not None:
                    print("Somma degli array:\n", somma)

            case "4":
                somma_totale = spazio.somma_totale()
                if somma_totale is not None:
                    print(f"La somma totale è: {somma_totale:.3f}")

            case "5":
                if spazio.array_1 is not None:
                    print("Array 1:\n", spazio.array_1)
                else:
                    print("Array 1 non ancora creato.")

            case "6":
                if spazio.array_2 is not None:
                    print("Array 2:\n", spazio.array_2)
                else:
                    print("Array 2 non ancora creato.")

            case "7":
                print("Uscita dal programma.")
                break

            case "8":
                somma1, somma2 = spazio.somma_maggiori_di_5()
                if somma1 is not None:
                    print(f"Somma elementi > 5 in Array 1: {somma1:.3f}")
                    print(f"Somma elementi > 5 in Array 2: {somma2:.3f}")

            case "9":
                spazio.stampa_dettagli()

            case _:
                print("Scelta non valida. Inserisci un numero da 1 a 9.")

