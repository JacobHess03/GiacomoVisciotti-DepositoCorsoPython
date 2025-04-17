# Esercizio 1

import numpy as np

# Crea un array di 15 numeri casuali interi tra 1 e 100
array = np.random.randint(1, 101, size=15)

# Calcola la somma degli elementi
somma = np.sum(array)

# Calcola la media degli elementi
media = np.mean(array)

# Stampa i risultati
print("Array generato:", array)
print("Somma degli elementi:", somma)
print("Media degli elementi:", media)
