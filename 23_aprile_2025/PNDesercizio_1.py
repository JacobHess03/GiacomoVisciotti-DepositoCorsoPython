import pandas as pd
import numpy as np
import openpyxl
# Definizione classe per le funzioni

class Conversion:
   
    def __init__(self, df):
       self.df = df
       
    def conv_csv(self):
        self.df.to_csv("prodotti.csv")
    
    def conv_json(self):
        self.df.to_json("prodotti.json")
        
    def conv_excel(self):
        self.df.to_excel("prodotti.xlsx")
    



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
# Dataframe
print("Dataframe Totale")
print(df, "\n")

# Stampa dei risultati
print("Prime 10 righe del DataFrame:")
print(df.head(10), "\n")

print("Pivot Table: media delle vendite per città e prodotto")
print(pivot_table, "\n")

print("Vendite Totali per Prodotto")
print(groupby_total)

# Conversione a csv
df.to_csv("prodotti.csv")


def main():
    
    C = Conversion(df)
    while(True):
        scelta = input("In che formato desideri convertire il dataframe: \n1. CSV\n2. Json\n3. Excel\n4. Esci\n")
        match scelta:
            case "1":
                C.conv_csv()
                print("CSV salvato.")
                
            case "2":
                
                C.conv_json()
                print("JSON salvato.")
            
            case "3":
                
                C.conv_excel()
                print("Excel salvato.")
                
            case "4":
                print("Uscita programma...")
                break
                
            
main()    