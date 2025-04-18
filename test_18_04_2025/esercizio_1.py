class Veicolo:
    def __init__(self, marca, anno, targa, revisione):
        self._marca = marca
        self._anno = anno
        self._targa = targa
        self._revisione = revisione

    def get_marca(self):
        return self._marca

    def get_anno(self):
        return self._anno

    def get_targa(self):
        return self._targa

    def get_revisione(self):
        return self._revisione

    def set_marca(self, marca):
        self._marca = marca

    def set_anno(self, anno):
        if anno > 1900:
            self._anno = anno
        else:
            raise ValueError("L'anno deve essere maggiore di 1900.")

    def set_targa(self, targa):
        if len(targa) >= 5:
            self._targa = targa
        else:
            raise ValueError("La targa deve essere almeno di 5 caratteri.")

    def set_revisione(self, revisione):
        self._revisione = revisione

    def descrivi(self):
        return (f"Veicolo: {self._marca}, Anno: {self._anno}, Targa: {self._targa}, "
                f"Revisione: {'OK' if self._revisione else 'Scaduta'}")

class Auto(Veicolo):
    def __init__(self, marca, anno, targa, revisione, porte):
        super().__init__(marca, anno, targa, revisione)
        self._porte = porte

    def get_porte(self):
        return self._porte

    def set_porte(self, porte):
        if porte > 0:
            self._porte = porte
        else:
            raise ValueError("Il numero di porte deve essere positivo.")

    def descrivi(self):
        base = super().descrivi()
        return f"Auto -> {base}, Porte: {self._porte}"

class Moto(Veicolo):
    def __init__(self, marca, anno, targa, revisione, cilindrata):
        super().__init__(marca, anno, targa, revisione)
        self._cilindrata = cilindrata

    def get_cilindrata(self):
        return self._cilindrata

    def set_cilindrata(self, cilindrata):
        if cilindrata > 0:
            self._cilindrata = cilindrata
        else:
            raise ValueError("La cilindrata deve essere positiva.")

    def descrivi(self):
        base = super().descrivi()
        return f"Moto -> {base}, Cilindrata: {self._cilindrata}cc"

class Camion(Veicolo):
    def __init__(self, marca, anno, targa, revisione, capacita):
        super().__init__(marca, anno, targa, revisione)
        self._capacita = capacita

    def get_capacita(self):
        return self._capacita

    def set_capacita(self, capacita):
        if capacita > 0:
            self._capacita = capacita
        else:
            raise ValueError("La capacità deve essere un valore positivo.")

    def descrivi(self):
        base = super().descrivi()
        return f"Camion -> {base}, Capacità: {self._capacita}t"

def crea_veicolo():
    tipi = {'1': 'Auto', '2': 'Moto', '3': 'Camion'}
    print("Scegli il tipo di veicolo da creare:")
    for k, v in tipi.items():
        print(f"{k}. {v}")
    scelta = input("Opzione: ")
    if scelta not in tipi:
        print("Scelta non valida.")
        return None

    marca = input("Marca: ")
    anno = int(input("Anno di immatricolazione: "))
    targa = input("Targa: ")
    rev = input("Revisione OK? (s/n): ")
    revisione = True if rev.lower() == 's' else False

    if scelta == '1':
        porte = int(input("Numero di porte: "))
        return Auto(marca, anno, targa, revisione, porte)
    elif scelta == '2':
        cilindrata = int(input("Cilindrata (cc): "))
        return Moto(marca, anno, targa, revisione, cilindrata)
    else:
        capacita = float(input("Capacità (tonnellate): "))
        return Camion(marca, anno, targa, revisione, capacita)

def main():
    lista = []
    while True:
        print("\nMenu:")
        print("1. Aggiungi veicolo")
        print("2. Mostra tutti i veicoli")
        print("3. Esci")
        cmd = input("Scelta: ")

        if cmd == '1':
            try:
                v = crea_veicolo()
                if v:
                    lista.append(v)
                    print("Veicolo aggiunto con successo.")
            except Exception as e:
                print(f"Errore: {e}")
        elif cmd == '2':
            if not lista:
                print("Nessun veicolo presente.")
            else:
                i = 1
                for v in lista:
                    print(f"{i}. {v.descrivi()}")
                    i += 1
        elif cmd == '3':
            print("Uscita in corso...")
            break
        else:
            print("Comando non riconosciuto.")

if __name__ == "__main__":
    main()
