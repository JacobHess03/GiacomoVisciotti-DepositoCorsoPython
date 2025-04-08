import random
numeri = []
# Genera 5 numeri casuali da 1 a 20
for i in range(5):
    numeri.append(str(random.randint(1, 20)))
    
numeri_stringa = ",".join(numeri)

# Scrive i numeri nel file
with open("08_aprile_2025\\numeri.txt", "w") as file:
    
    file.write(numeri_stringa)

# Legge i numeri dal file
with open("08_aprile_2025\\numeri.txt", "r") as file:
    
    numeri_salvati = file.read()

numeri_saved = numeri_salvati.split(",")

# Chiede all'utente di indovinare 2 numeri
print("Prova a indovinare 2 numeri tra 1 e 20!")
indovinati = 0
for i in range(2):
    tentativo = input(f"Tentativo {i+1}: ")
    if tentativo in numeri_saved:
        indovinati += 1

# Verifica esito
if indovinati >= 2:
    print("Hai vinto!")
else:
    print("Hai perso!")

