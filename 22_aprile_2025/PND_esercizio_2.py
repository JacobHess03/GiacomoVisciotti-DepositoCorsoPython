import pandas as pd
import numpy as np

def genera_dataset():
    np.random.seed(0)
    prodotti = ['ProdottoA', 'ProdottoB', 'ProdottoC']
    città = ['Milano', 'Roma', 'Torino']
    
    # Generazione dati con range realistici per superare la soglia di 1000€
    df = pd.DataFrame({
        'Prodotto': np.random.choice(prodotti, 20),
        'Quantità': np.random.randint(50, 200, 20),  # Quantità aumentate
        'Prezzo Unitario': np.random.uniform(20.0, 100.0, 20).round(2),  # Prezzi aumentati
        'Città': np.random.choice(città, 20)
    })
    
    df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
    return df

def analisi_custom(df, pivot_column):
    try:
        # Verifica se la colonna esiste nel DataFrame
        if pivot_column not in df.columns:
            raise KeyError
        
        # Crea la pivot table con aggregazioni multiple
        pivot_result = df.pivot_table(
            index=pivot_column,
            values=['Quantità', 'Totale Vendite'],
            aggfunc={
                'Quantità': ['sum', 'mean', 'max'],
                'Totale Vendite': ['sum', 'mean', 'max', 'count']
            }
            
        ).round(2)
        
        return pivot_result
        
    except KeyError:
        return "Campo non valido! Usa uno di questi: " + ", ".join(df.columns)
def mostra_menu():
    print("\n" + "="*40)
    print("=== MENU ANALISI VENDITE ===")
    print("1. Visualizza dataset completo")
    print("2. Top 5 vendite")
    print("3. Prodotto più venduto (quantità)")
    print("4. Città con maggior fatturato")
    print("5. Vendite sopra soglia personalizzata")
    print("6. Statistiche per campo personalizzato")
    print("7. Esci")
    return input("\nSeleziona un'opzione (1-7): ")

def main():
    df = genera_dataset()
    df_ordinato = df.sort_values('Totale Vendite', ascending=False)
    
    while True:
        scelta = mostra_menu()
        
        match scelta:
            case '1':
                print("\n Dataset completo ")
                print(df)
            
            case '2':
                print("\n Top 5 vendite ")
                print(df_ordinato.head().format({
                    'Prezzo Unitario': '€ {:.2f}',
                    'Totale Vendite': '€ {:,.2f}'
                }))
            
            case '3':
                prodotto_top = df.groupby('Prodotto')['Quantità'].sum().idxmax()
                qta = df.groupby('Prodotto')['Quantità'].sum().max()
                print(f"\n● Prodotto più venduto \n{prodotto_top} - {qta} unità")
            
            case '4':
                citta_top = df.groupby('Città')['Totale Vendite'].sum().idxmax()
                totale = df.groupby('Città')['Totale Vendite'].sum().max()
                print(f"\n Città con maggior fatturato \n{citta_top} - € {totale:,.2f}")
            
            case '5':
                soglia = float(input("Inserisci la soglia (es. 1000): "))
                vendite_sopra = df[df['Totale Vendite'] > soglia]
                print(f"\n Vendite sopra € {soglia:,.2f} ")
                print(vendite_sopra if not vendite_sopra.empty else "Nessuna vendita trovata")
            
            case '6':
                print(f"\nCampi disponibili: Prodotto, Prezzo Unitario, Città")
                campo = input("Inserisci il campo per il raggruppamento: ")
                risultato = analisi_custom(df, campo)
                print(risultato)
            
            case '7':
                print("\nUscita programma...")
                break
            
            case _:
                print("\nScelta non valida, riprova!")

if __name__ == "__main__":
    main()