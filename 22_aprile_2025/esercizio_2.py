import pandas as pd
import numpy as np

# -----------------------------
# Esercizio 1: Analisi Esplorativa dei Dati
# -----------------------------
# Obiettivo: esplorare un dataset casuale di persone
# con Nome, Età, Città, Salario, con duplicati e valori mancanti.

# 1. Generazione del DataFrame con valori casuali e inserimento di duplicati e NaN
np.random.seed(42)
num_rows = 15

# Creazione colonne base
nomi = [f"Persona {i}" for i in range(1, num_rows+1)]
età = np.random.randint(18, 80, size=num_rows).astype(float)
città = np.random.choice(["Roma", "Milano", "Napoli", "Torino", None], size=num_rows)
salari = np.round(np.random.uniform(20000, 80000, size=num_rows), 2)

# Dataset con duplicati e missing
df = pd.DataFrame({
    "Nome": nomi + ["Persona 1", "Persona 2"],
    "Età": np.concatenate([età, [np.nan, età[1]]]),
    "Città": np.concatenate([città, ["Roma", None]]),
    "Salario": np.concatenate([salari, [50000, np.nan]])
})

# 2. Visualizzazione delle prime e ultime 5 righe
def esplora_head_tail(dataframe):
    print("Prime 5 righe:")
    print(dataframe.head(), "\n")
    print("Ultime 5 righe:")
    print(dataframe.tail(), "\n")

# 3. Tipi di dato di ciascuna colonna
def mostra_dtypes(dataframe):
    print("Tipi di dato:")
    print(dataframe.dtypes, "\n")

# 4. Statistiche descrittive di base
def statistiche_descrittive(dataframe):
    print("Statistiche descrittive (numeriche):")
    print(dataframe.describe(), "\n") # Describe -> quanti valori non nulli per colonna, media aritmetica per colonna, Dev std, min, max, 25%, 50%, 75%

# 5. Rimozione duplicati per nome
def rimuovi_duplicati(dataframe):
    print(f"Righe prima della rimozione duplicati: {len(dataframe)}")
    # Rimuove le righe duplicate basandosi sul campo 'Nome', mantenendo la prima occorrenza
    df_clean = dataframe.drop_duplicates(subset=['Nome'], keep='first')
    print(f"Righe dopo rimozione duplicati (per Nome): {len(df_clean)}\n")
    return df_clean

# 6. Gestione valori mancanti con mediana e sostituzione Città
def gestisci_missing(dataframe):
    # Calcolo mediana per Età e Salario
    med_età = dataframe["Età"].median()
    med_sal = dataframe["Salario"].median()
    # Sostituzione valori NaN e None
    dataframe = dataframe.fillna({"Età": med_età, "Salario": med_sal, "Città": "Città X", "Nome": "Perona X" })
    print(f"Valori mancanti sostituiti: Età->{med_età}, Salario->{med_sal}, Città->'Città X', Nome-> 'Persona X'\n")
    return dataframe

# 7. Aggiunta colonna Categoria Età
def categoria_età(age):
    if age <= 18:
        return "Giovane"
    elif age <= 65:
        return "Adulto"
    else:
        return "Senior"

def aggiungi_categoria(dataframe):
    dataframe["Categoria Età"] = dataframe["Età"].apply(categoria_età)
    print("Colonna 'Categoria Età' aggiunta.\n")
    return dataframe

# 8. Salvataggio in CSV
OUTPUT_CSV = "people_clean.csv"
def salva_csv(dataframe, path=OUTPUT_CSV):
    dataframe.to_csv(path, index=False)
    print(f"DataFrame pulito salvato in: {path}")

# Funzione principale di esecuzione
if __name__ == "__main__":
    df_originale = df.copy()
    esplora_head_tail(df_originale)
    mostra_dtypes(df_originale)
    statistiche_descrittive(df_originale)

    df_no_dup = rimuovi_duplicati(df_originale)
    df_no_missing = gestisci_missing(df_no_dup)
    df_finale = aggiungi_categoria(df_no_missing)

    salva_csv(df_finale)

    print("\nEsercizio 1 completato con successo.")
