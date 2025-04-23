import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Generazione del DataFrame con temperature giornaliere

def generate_temperature_data(days: int = 30, seed: int = 42):
    """
    Genera un DataFrame con una colonna 'temperature' contenente valori casuali
    di temperatura tra 0 e 35 °C per il numero di giorni specificato.
    """
    np.random.seed(seed)
    temperatures = np.random.uniform(low=0.0, high=35.0, size=days)
    df = pd.DataFrame({'temperature': np.round(temperatures, 2)})
    return df

# 2. Calcolo delle statistiche

def compute_statistics(df: pd.DataFrame):
    """
    Calcola massimo, minimo, media e mediana delle temperature.
    Restituisce un dizionario con le statistiche.
    """
    stats = {
        'Max': df['temperature'].max(),
        'Min': df['temperature'].min(),
        'Mean': df['temperature'].mean(),
        'Median': df['temperature'].median()
    }
    return stats

# 3. Funzione per il grafico di un singolo valore sul time series
def plot_statistic(df: pd.DataFrame, stat_name: str, stat_value: float):
    """
    Crea un grafico con giorni sull'asse x e temperature sull'asse y,
    evidenziando il valore della statistica con una linea orizzontale.
    """
    days = np.arange(1, len(df) + 1)
    plt.figure(figsize=(6, 4))
    plt.plot(days, df['temperature'], marker='o')
    plt.axhline(stat_value, linestyle='--', label=f"{stat_name}: {stat_value:.2f} °C")
    plt.title(f"Serie delle temperature e {stat_name}")
    plt.xlabel('Giorno del mese')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 4. Funzione principale

def main():
    # Genera i dati
    df_temps = generate_temperature_data(days=30)

    # Statistiche descrittive con describe()
    print("Statistiche descrittive complete:")
    print(df_temps['temperature'].describe(), "\n")

    # Calcola le statistiche
    stats = compute_statistics(df_temps)
    for name, value in stats.items():
        print(f"{name}: {value:.2f} °C")

    # 4 figure separate con giorni-ascisse e temperature-ordinate
    for name, value in stats.items():
        plot_statistic(df_temps, name, value)

if __name__ == "__main__":
    main()
