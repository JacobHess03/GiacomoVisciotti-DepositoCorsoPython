import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

# Genera un dataset di esempio
np.random.seed(42)
n = 100  # numero di clienti

data = {
    "ID_Cliente": np.arange(1, n + 1),
    "Età": np.random.randint(18, 80, size=n),
    "Durata_Abbonamento": np.random.randint(1, 60, size=n),
    "Tariffa_Mensile": np.round(np.random.uniform(10, 100, size=n), 2),
    "Dati_Consumati": np.round(np.random.uniform(1, 50, size=n), 2),
    "Servizio_Clienti_Contatti": np.random.randint(0, 10, size=n),
    "Churn": np.random.choice(["Sì", "No"], size=n, p=[0.3, 0.7])
}

df = pd.DataFrame(data)

# Salva su CSV
output_path = "telecom_churn.csv"
df.to_csv(output_path, index=False)



def load_data(filepath: str):
    """
    Carica il dataset da un file CSV.
    """
    df = pd.read_csv(filepath)
    return df


def explore_data(df: pd.DataFrame):
    """
    Esplorazione iniziale dei dati: info, descrizione e distribuzioni.
    """
    print("Informazioni generali:")
    print(df.info(), "\n")
    print("Statistiche descrittive:")
    print(df.describe(), "\n")
    print("Distribuzione Churn:")
    print(df['Churn'].value_counts(), "\n")


def clean_data(df: pd.DataFrame):
    """
    Pulizia dei dati: gestione valori mancanti e anomalie.
    """
    # Rimuovi righe con valori mancanti
    df_clean = df.dropna().copy()

    # Correggi anomalie: età negative o troppo grandi
    valid_age_mask = (df_clean['Età'] >= 18) & (df_clean['Età'] <= 100)
    df_clean = df_clean.loc[valid_age_mask]

    # Correggi anomalie: tariffa mensile > 0
    df_clean = df_clean[df_clean['Tariffa_Mensile'] > 0]

    return df_clean


def engineer_features(df: pd.DataFrame):
    """
    Crea nuove colonne utili all'analisi.
    """
    df = df.copy()
    df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
    return df


def analyze_correlations(df: pd.DataFrame):
    """
    Analizza correlazioni tra variabili numeriche.
    """
    numeric = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']
    corr_matrix = df[numeric].corr()
    print("Matrice di correlazione:")
    print(corr_matrix, "\n")


def prepare_for_modeling(df: pd.DataFrame):
    """
    Prepara i dati per il modello: codifica churn e normalizzazione.
    """
    df_model = df.copy()

    # Codifica Churn: No->0, Sì->1
    df_model['Churn_Flag'] = df_model['Churn'].map({'No': 0, 'Sì': 1})

    # Seleziona variabili predittive
    features = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']
    X = df_model[features].values.astype(float)
    y = df_model['Churn_Flag'].values

    # Normalizzazione manuale con numpy
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X_norm = (X - X_mean) / X_std

    return X_norm, y


def train_and_evaluate(X: np.ndarray, y: np.ndarray):
    """
    Addestra un modello di regressione logistica e valuta le prestazioni.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    print("VALORI DI TEST: ")
    print(y_test)
    print("VALORI DI PREDIZIONE: ")
    print(y_pred)
    print("VALORI DI PROBABILITA'")
    print(y_prob)
    print("\nCONFRONTO DETTAGLIATO:")
    print("{:<7} {:<10} {:<10} {:<15}".format("Index", "Actual", "Predicted", "Probability(Churn=1)"))
    print("-" * 45)

    for i, (actual, pred, prob) in enumerate(zip(y_test, y_pred, y_prob)):
        print("{:<7} {:<10} {:<10} {:<15.4f}".format(i, actual, pred, prob))
        accuracy = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)

    print(f"Accuratezza del modello: {accuracy:.3f}")
    print(f"AUC: {auc:.3f}")


def main():
    # Percorso al file CSV
    filepath = "telecom_churn.csv"

    # Caricamento e esplorazione
    df = load_data(filepath)
    explore_data(df)

    # Pulizia e feature engineering
    df_clean = clean_data(df)
    df_feat = engineer_features(df_clean)

    # Analisi EDA e correlazioni
    analyze_correlations(df_feat)

    # Preparazione e modellazione
    X, y = prepare_for_modeling(df_feat)
    train_and_evaluate(X, y)

if __name__ == "__main__":
    main()
