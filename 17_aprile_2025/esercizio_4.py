import numpy as np

def menu_range_array():
    print("=== MENU CREAZIONE ARRAY NUMPY CON RANGE ===")
    try:
        start = int(input("Inserisci il valore di START: "))
        stop = int(input("Inserisci il valore di STOP: "))
        step = int(input("Inserisci il valore di STEP: "))

        if step == 0:
            print("ERRORE: Lo STEP non può essere 0.")
            return None

        array = np.arange(start, stop, step)
        print("\nArray creato:")
        print(array)

        return array

    except ValueError:
        print("ERRORE: Inserisci solo numeri interi validi.")
        return None

def menu_reshape_array(array):
    print("\n=== MENU RESHAPE ARRAY ===")
    risposta = input("Vuoi eseguire il reshape dell'array? (s/n): ").strip().lower()

    if risposta != 's':
        print("Uscita dal menu reshape.")
        return

    try:
        rows = int(input("Inserisci il numero di righe desiderato: "))
        cols = int(input("Inserisci il numero di colonne desiderato: "))

        if rows * cols != array.size:
            print(f"ERRORE: Il reshape {rows}x{cols} non è compatibile con un array di {array.size} elementi.")
            return

        reshaped = array.reshape(rows, cols)
        print("\nArray reshape:")
        print(reshaped)

    except ValueError:
        print("ERRORE: Inserisci solo numeri interi validi.")

# Esecuzione del programma
array_creato = menu_range_array()
if array_creato is not None:
    menu_reshape_array(array_creato)
