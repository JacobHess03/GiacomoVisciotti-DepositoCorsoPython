# Sales Analysis System

## Scopo
Sistema interattivo per l'analisi di dati di vendita simulati con:
- Generazione automatica dataset
- Menu interattivo
- Funzioni di analisi avanzate

## Funzionalità principali
- 🗂 Visualizzazione dataset completo
- 📊 Top 5 vendite
- 🏆 Identificazione prodotto più venduto
- 🌆 Classifica città per fatturato
- 🔍 Filtro vendite per soglia personalizzata
- 📈 Pivot table personalizzabili

## Prerequisiti
- Python 3.10+
- Librerie richieste:
  ```bash
  pip install pandas numpy
  ```

## Utilizzo
1. Clona il repository
2. Esegui lo script:
   ```bash
   python sales_analysis.py
   ```
3. Segui le istruzioni del menu

## Opzioni del Menu
| Opzione | Descrizione                          |
|---------|--------------------------------------|
| 1       | Mostra tutto il dataset              |
| 2       | Visualizza top 5 vendite             |
| 3       | Prodotto con maggiori quantità vendute |
| 4       | Città con maggior fatturato          |
| 5       | Filtra vendite per soglia            |
| 6       | Analisi personalizzata               |
| 7       | Esci                                 |

## Esempio Analisi Personalizzata
```
Seleziona un'opzione (1-7): 6

Campi disponibili: Prodotto, Prezzo Unitario, Città
Inserisci il campo per il raggruppamento: Città

                Quantità          Totale Vendite          
                   sum   mean max       sum    mean    max
Città                                                     
Milano           1502  150.2 198  89,452.33 8,945.23 15,000.00
Roma             1623  162.3 195  95,678.45 9,567.84 16,500.00
Torino           1578  157.8 200  92,345.67 9,234.57 17,000.00
```

## Note
- I dati sono generati casualmente ad ogni esecuzione
- Il seed è fissato per riproducibilità
- Formattazione automatica dei valori monetari
