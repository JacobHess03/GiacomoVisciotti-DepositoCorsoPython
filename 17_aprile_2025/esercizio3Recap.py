import numpy as np

# Crea un array 4x4 con numeri interi casuali tra 10 e 50
array = np.random.randint(10, 51, size=(4, 4))

# Fancy indexing: seleziona gli elementi agli indici (0,1), (1,3), (2,2), (3,0)
righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]
elementi_selezionati = array[righe, colonne]

# Seleziona tutte le righe dispari
righe_dispari = array[0::2]  # partendo da riga 1, ogni 2 righe

# Modifica: aggiungi 10 agli elementi selezionati
array[righe, colonne] += 10

# Stampa dei risultati
print("Array originale modificato:\n", array)
print("Elementi selezionati con fancy indexing (dopo +10):", array[righe, colonne])
print("Righe dispari:\n", righe_dispari)
