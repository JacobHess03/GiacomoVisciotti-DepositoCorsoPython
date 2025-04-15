class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        self.__titolare = None
        self.__saldo = 0.0
        self.set_titolare(titolare)
        try:
            saldo = float(saldo_iniziale)
            if saldo >= 0:
                self.__saldo = saldo
        except:
            pass

    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nuovo_titolare):
        if type(nuovo_titolare) == str and nuovo_titolare.strip() != "":
            self.__titolare = nuovo_titolare.strip()
        else:
            raise ValueError("Il titolare deve essere una stringa non vuota.")

    def set_deposita(self, importo):
        try:
            importo = float(importo)
            if importo > 0:
                self.__saldo += importo
            else:
                raise ValueError
        except:
            raise ValueError("L'importo da depositare deve essere un numero positivo.")

    def set_preleva(self, importo):
        try:
            importo = float(importo)
            if importo > 0 and self.__saldo >= importo:
                self.__saldo -= importo
            elif importo <= 0:
                raise ValueError("L'importo deve essere positivo.")
            else:
                raise ValueError("Fondi insufficienti.")
        except:
            raise ValueError("L'importo da prelevare deve essere un numero valido e positivo.")

    def get_saldo(self):
        return round(self.__saldo, 2)


# Menu interattivo
def menu():
    print("Benvenuto! Crea il tuo conto bancario.")
    titolare = input("Inserisci il nome del titolare: ")
    saldo_iniziale = input("Inserisci il saldo iniziale: ")
    conto = ContoBancario(titolare, saldo_iniziale)

    while True:
        print("\n--- MENU CONTO BANCARIO ---")
        print("1. Visualizza saldo")
        print("2. Deposita")
        print("3. Preleva")
        print("4. Mostra titolare")
        print("5. Modifica titolare")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                print(f"Saldo attuale: {conto.get_saldo():.2f} €")
            case "2":
                importo = input("Inserisci l'importo da depositare: ")
                try:
                    conto.set_deposita(importo)
                    print("Deposito effettuato con successo.")
                except ValueError as e:
                    print(f"Errore: {e}")
            case "3":
                importo = input("Inserisci l'importo da prelevare: ")
                try:
                    conto.set_preleva(importo)
                    print("Prelievo effettuato con successo.")
                except ValueError as e:
                    print(f"Errore: {e}")
            case "4":
                print(f"Titolare del conto: {conto.get_titolare()}")
            case "5":
                nuovo_nome = input("Inserisci il nuovo nome del titolare: ")
                try:
                    conto.set_titolare(nuovo_nome)
                    print("Titolare aggiornato con successo.")
                except ValueError as e:
                    print(f"Errore: {e}")
            case "0":
                print("Uscita in corso... Grazie per aver usato il nostro servizio.")
                break
            case _:
                print("Opzione non valida. Riprova.")

# Avvio del programma
if __name__ == "__main__":
    menu()
