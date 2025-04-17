import numpy as np

# Crea una matrice 5x5 con numeri da 1 a 25
matrice = np.arange(1, 26).reshape(5, 5)

# Estrai la seconda colonna (indice 1)
seconda_colonna = matrice[:, 1]

# Estrai la terza riga (indice 2)
terza_riga = matrice[2, :]

# Calcola la somma della diagonale principale
somma_diagonale = np.trace(matrice)

# Stampa i risultati
print("Matrice 5x5:\n", matrice)
print("Seconda colonna:", seconda_colonna)
print("Terza riga:", terza_riga)
print("Somma della diagonale principale:", somma_diagonale)
