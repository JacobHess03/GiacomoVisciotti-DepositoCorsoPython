import sqlite3

conn = sqlite3.connect("zoo.db")
cursor = conn.cursor()

# Tabella base Animale
cursor.execute("""
CREATE TABLE IF NOT EXISTS Animali (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    eta INTEGER NOT NULL,
    specie TEXT NOT NULL  -- Leone, Giraffa, Pinguino
);
""")

# Leone
cursor.execute("""
CREATE TABLE IF NOT EXISTS Leoni (
    id INTEGER PRIMARY KEY,
    tipo TEXT,
    lun_artigli REAL,
    FOREIGN KEY(id) REFERENCES Animali(id)
);
""")

# Giraffa
cursor.execute("""
CREATE TABLE IF NOT EXISTS Giraffe (
    id INTEGER PRIMARY KEY,
    tipo TEXT,
    lun_collo REAL,
    FOREIGN KEY(id) REFERENCES Animali(id)
);
""")

# Pinguino
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pinguini (
    id INTEGER PRIMARY KEY,
    tipo TEXT,
    v_water REAL,
    lun_pinne REAL,
    FOREIGN KEY(id) REFERENCES Animali(id)
);
""")




# Stampa l'elenco delle tabelle
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelle = cursor.fetchall()
print("Tabelle presenti nel database:")
for tabella in tabelle:
    print("-", tabella[0])

# Stampa lo schema di ogni tabella
for tabella in tabelle:
    print(f"\nSchema della tabella {tabella[0]}:")
    cursor.execute(f"PRAGMA table_info({tabella[0]});")
    colonne = cursor.fetchall()
    for colonna in colonne:
        print(colonna)

conn.commit()
conn.close()
