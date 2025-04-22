import pandas as pd
import numpy as np

# 1. Generazione dei Dati con array, senza liste
np.random.seed(42)  # Per riproducibilità

# Definizione degli assi
dates = pd.date_range(start='2025-03-01', periods=30, freq='D')
cities = np.array(['Milano', 'Roma', 'Torino'])
products = np.array(['Prodotto A', 'Prodotto B', 'Prodotto C'])

# Calcolo del numero totale di righe
n_dates = len(dates)
n_cities = len(cities)
n_products = len(products)
n_rows = n_dates * n_cities * n_products

# Costruzione dei vettori "espansi"
date_col = np.repeat(dates.values, n_cities * n_products)
city_col = np.tile(np.repeat(cities, n_products), n_dates)
product_col = np.tile(products, n_dates * n_cities)

# Generazione casuale delle vendite
sales_col = np.random.randint(100, 500, size=n_rows)

# Creazione del DataFrame da dizionario di array
df = pd.DataFrame({
    'Data': date_col,
    'Città': city_col,
    'Prodotto': product_col,
    'Vendite': sales_col
})

# 2. Creazione della Tabella Pivot (media delle vendite per città e prodotto)
pivot_table = df.pivot_table(
    index='Città',
    columns='Prodotto',
    values='Vendite',
    aggfunc='mean'
)

# 3. GroupBy delle Vendite Totali per Prodotto
groupby_total = df.groupby('Prodotto', as_index=False)['Vendite'].sum()

# Stampa dei risultati
print("Prime 10 righe del DataFrame:")
print(df.head(10), "\n")

print("Pivot Table: media delle vendite per città e prodotto")
print(pivot_table, "\n")

print("Vendite Totali per Prodotto")
print(groupby_total)
