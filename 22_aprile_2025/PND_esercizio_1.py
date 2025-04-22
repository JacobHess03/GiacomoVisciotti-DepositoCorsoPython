import pandas as pd
import numpy as np

# 1. Generazione dei Dati
np.random.seed(42)  # Per riproducibilità
dates = pd.date_range(start='2025-03-01', periods=30, freq='D')
cities = ['Milano', 'Roma', 'Torino']
products = ['Prodotto A', 'Prodotto B', 'Prodotto C']

data = []
for date in dates:
    for city in cities:
        for product in products:
            sales = np.random.randint(100, 500)
            data.append({
                'Data': date,
                'Città': city,
                'Prodotto': product,
                'Vendite': sales
            })

df = pd.DataFrame(data)

# Mostra le prime righe del DataFrame per verifica
print("Prime 10 righe del DataFrame:")
print(df.head(10), "\n")

# 2. Creazione della Tabella Pivot
pivot_table = df.pivot_table(
    index='Città',
    columns='Prodotto',
    values='Vendite',
    aggfunc='mean'
)

print("Pivot Table: media delle vendite per città e prodotto")
print(pivot_table, "\n")

# 3. GroupBy delle Vendite Totali per Prodotto
groupby_total = df.groupby('Prodotto')['Vendite'].sum()

print("Vendite Totali per Prodotto")
print(groupby_total)
