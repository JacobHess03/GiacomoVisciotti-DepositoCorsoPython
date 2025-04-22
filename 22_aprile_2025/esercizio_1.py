import sqlite3
import numpy as np
import os

DB_FILE = 'analysis.db'
NUM_ROWS = 10


def connect_db(db_file):
    """
    Connessione al database SQLite (file) e ritorno della connessione.
    """
    conn = sqlite3.connect(db_file)
    print(f"Connesso al database SQLite: {db_file}")
    return conn


def setup_tables(conn):
    """
    Crea tabelle clienti, ordini, pagamenti e stati, cancellandole se esistono già.
    """
    cur = conn.cursor()
    # Rimozione vecchie tabelle
    cur.execute("DROP TABLE IF EXISTS pagamenti;")
    cur.execute("DROP TABLE IF EXISTS ordini;")
    cur.execute("DROP TABLE IF EXISTS clienti;")
    cur.execute("DROP TABLE IF EXISTS stati;")

    # Creazione tabella clienti con id, età e nome
    cur.execute(
        '''
        CREATE TABLE clienti (
            id INTEGER PRIMARY KEY,
            eta INTEGER,
            nome TEXT
        )
        '''
    )
    # Creazione tabella ordini con id, riferimento cliente e prodotto
    cur.execute(
        '''
        CREATE TABLE ordini (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            prodotto TEXT
        )
        '''
    )
    # Creazione tabella pagamenti con id, riferimento ordine e importo
    cur.execute(
        '''
        CREATE TABLE pagamenti (
            id INTEGER PRIMARY KEY,
            ordine_id INTEGER,
            importo REAL
        )
        '''
    )
    # Creazione tabella stati con id e nome dello stato
    cur.execute(
        '''
        CREATE TABLE stati (
            id INTEGER PRIMARY KEY,
            nome TEXT
        )
        '''
    )
    conn.commit()
    print("Tabelle clienti, ordini, pagamenti e stati create.")


def popola_tabelle(conn, n):
    """
    Popola clienti, ordini e pagamenti con dati fittizi.
    """
    cur = conn.cursor()
    importi = np.linspace(0, 50, n)
    eta_vals = np.random.randint(18, 66, size=n)

    for i in range(1, n + 1):
        cur.execute(
            "INSERT INTO clienti (id, eta, nome) VALUES (?, ?, ?)",
            (i, int(eta_vals[i-1]), f"Cliente {i}")
        )
        cur.execute(
            "INSERT INTO ordini (id, cliente_id, prodotto) VALUES (?, ?, ?)",
            (i, i, f"Prodotto {i}")
        )
        cur.execute(
            "INSERT INTO pagamenti (id, ordine_id, importo) VALUES (?, ?, ?)",
            (i, i, float(importi[i-1]))
        )
    conn.commit()
    print(f"Inseriti {n} clienti, ordini e pagamenti.")


def popola_tabelle_stati(conn, n):
    """
    Popola la tabella stati con N nomi fittizi (es. Stato1, Stato2...).
    """
    cur = conn.cursor()
    for i in range(1, n + 1):
        cur.execute(
            "INSERT INTO stati (id, nome) VALUES (?, ?)",
            (i, f"Stato{i}")
        )
    conn.commit()
    print(f"Inseriti {n} stati nella tabella stati.")


def link_states(conn):
    """
    Chiede all'utente a quale tabella collegare gli stati e aggiunge la colonna stato_id.
    Popola in base all'id corrispondente.
    """
    cur = conn.cursor()
    print("\n-- Collegamento stati --")
    print("1. Clienti")
    print("2. Ordini")
    print("3. Pagamenti")
    choice = input("Seleziona la tabella a cui aggiungere lo stato (1-3): ")

    table_map = {'1': 'clienti', '2': 'ordini', '3': 'pagamenti'}
    if choice not in table_map:
        print("Scelta non valida, nessun collegamento effettuato.")
        return
    table = table_map[choice]

    try:
        cur.execute(f"ALTER TABLE {table} ADD COLUMN stato_id INTEGER;")
    except sqlite3.OperationalError:
        pass

    cur.execute(f"SELECT id FROM {table};")
    for (row_id,) in cur.fetchall():
        cur.execute(
            f"UPDATE {table} SET stato_id = ? WHERE id = ?;",
            (row_id, row_id)
        )
    conn.commit()
    print(f"Tabella '{table}' aggiornata con stato_id.")


def estrai_importi(conn):
    cur = conn.cursor()
    cur.execute('''SELECT importo FROM pagamenti ORDER BY id''')
    return np.array([r[0] for r in cur.fetchall()], dtype=float)


def estrai_eta(conn):
    cur = conn.cursor()
    cur.execute('''SELECT eta FROM clienti ORDER BY id''')
    return np.array([r[0] for r in cur.fetchall()], dtype=int)


def estrai_dati_rel(conn):
    cur = conn.cursor()
    cur.execute(
        '''
        SELECT c.nome, c.eta, o.prodotto, p.importo, s.nome
        FROM clienti c
        LEFT JOIN ordini o ON c.id = o.cliente_id
        LEFT JOIN pagamenti p ON o.id = p.ordine_id
        LEFT JOIN stati s ON s.id = c.id
        ORDER BY c.id
        '''
    )
    return cur.fetchall()


def main():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = connect_db(DB_FILE)
    setup_tables(conn)
    popola_tabelle(conn, NUM_ROWS)
    popola_tabelle_stati(conn, NUM_ROWS)

    # Menu principale
    while True:
        print("\n--- Menu Principale ---")
        print("1. Collegamento Stati")
        print("2. Analisi Dati")
        print("0. Esci")
        main_choice = input("Scelta: ")

        match main_choice:
            case '0':
                print("Uscita.")
                break
            case '1':
                link_states(conn)
                continue
            case '2':
                # Sottomenu Analisi Dati
                while True:
                    print("\n--- Seleziona il dataset ---")
                    print("1. Importi")
                    print("2. Età clienti")
                    print("3. Mostra dati relazionati")
                    print("0. Torna al menu principale")
                    choice = input("Scelta dataset: ")

                    match choice:
                        case '0':
                            break
                        case '1':
                            valori = estrai_importi(conn)
                        case '2':
                            valori = estrai_eta(conn)
                        case '3':
                            dati = estrai_dati_rel(conn)
                            print("\n--- Dati Relazionati ---")
                            for r in dati:
                                print(f"Cliente: {r[0]}, Età: {r[1]}, Prodotto: {r[2]}, Importo: {r[3]}, Stato: {r[4]}")
                            continue
                        case _:
                            print("Scelta non valida, riprova.")
                            continue

                    # Menu operazioni sul dataset scelto
                    while True:
                        print("\n--- Operazioni ---")
                        print("1. Somma")
                        print("2. Media")
                        print("3. Mediana")
                        print("4. Varianza")
                        print("5. Mostra grezzi")
                        print("0. Torna indietro")
                        op = input("Scelta operazione: ")

                        match op:
                            case '0':
                                break
                            case '1':
                                print(f"Somma: {np.sum(valori)}")
                            case '2':
                                print(f"Media: {np.mean(valori)}")
                            case '3':
                                print(f"Mediana: {np.median(valori)}")
                            case '4':
                                print(f"Varianza: {np.var(valori)}")
                            case '5':
                                print(valori)
                            case _:
                                print("Operazione non valida")
            case _:
                print("Scelta non valida, riprova.")

    conn.close()


if __name__ == '__main__':
    main()
