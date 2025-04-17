
import numpy as np
import sqlite3

# 1. Crea una matrice 6x6 con numeri interi casuali tra 1 e 100
matrice = np.random.randint(1, 101, size=(6, 6))

# 2. Estrai la sotto-matrice centrale 4x4
sottomatrice = matrice[1:5, 1:5]

# 3. Inverti le righe della sottomatrice
sottomatrice_invertita = sottomatrice[::-1]

# 4. Estrai la diagonale principale della matrice invertita usando indexing
indici = np.arange(4)
diagonale = sottomatrice_invertita[indici, indici]
# oppure con diag
print(diagonale)
# 5. Sostituisci i multipli di 3 con -1 usando indexing 
sottomatrice_modificata = sottomatrice_invertita.copy()
# Easy way
maschera = sottomatrice_modificata % 3 == 0
sottomatrice_modificata = sottomatrice_invertita[maschera] = -1
# # Bad way
# for i in range(4):
#     for j in range(4):
#         if sottomatrice_modificata[i, j] % 3 == 0:
#             sottomatrice_modificata[i, j] = -1

# 6. Stampa i risultati
print("Matrice originale 6x6:\n", matrice)
print("\nSotto-matrice centrale 4x4:\n", sottomatrice)
print("\nSotto-matrice invertita (righe invertite):\n", sottomatrice_invertita)
print("\nDiagonale principale della matrice invertita (con indexing):\n", diagonale)
print("\nSotto-matrice modificata (multipli di 3 sostituiti con -1):\n", sottomatrice_modificata)



# Connessione al database
conn = sqlite3.connect(":memory:")  # puoi usare anche un file SQLite invece di :memory:
cur = conn.cursor()

# Creazione della tabella Matrice
cur.execute("""
CREATE TABLE IF NOT EXISTS Matrice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 INTEGER,
    col2 INTEGER,
    col3 INTEGER,
    col4 INTEGER,
    col5 INTEGER,
    col6 INTEGER
)
""")

# Esempio di matrice 6x6
dati = [
    (10, 20, 30, 40, 50, 60),
    (70, 80, 90, 100, 110, 120),
    (130, 140, 150, 160, 170, 180),
    (190, 200, 210, 220, 230, 240),
    (250, 260, 270, 280, 290, 300),
    (310, 320, 330, 340, 350, 360)
]

# Inserimento dei dati nella tabella
cur.executemany("INSERT INTO Matrice (col1, col2, col3, col4, col5, col6) VALUES (?, ?, ?, ?, ?, ?)", dati)

# Commit per salvare i cambiamenti
conn.commit()


# Seleziona tutte le righe della tabella
cur.execute("SELECT col1, col2, col3, col4, col5, col6 FROM Matrice")
rows = np.array(cur.fetchall())  # Converte il risultato in un array NumPy

# Stampa la matrice
print("Matrice 6x6 ottenuta dal DB:")
print(rows)

# Chiudi la connessione
conn.close()
