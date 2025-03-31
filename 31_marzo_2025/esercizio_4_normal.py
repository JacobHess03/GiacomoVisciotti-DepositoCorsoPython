
lista = []
i = 0
flag = True
while (flag):
    seleziona = input("Vuoi continuare? (s/n)")
    if seleziona.lower() == "no":
        flag = False
    else:    
        elem = int(input("Inserisci il numero"))
        lista.insert(i, elem)
        print(lista[i])
        i += 1
# Se la lista è vuota
if not lista:
    print("Lista Vuota")
else:
    #Trovo il numero massimo usando un ciclo for
    massimo = lista[0]
    for num in lista:
        if num > massimo:
            massimo = num

    #Conto il numero di elementi usando un ciclo while
    count = 0
    i = 0
    while i < len(lista):
        count += 1
        i += 1

    #Stampo i risultati
    print(f"Numero massimo: {massimo}")
    print(f"Numero di elementi nella lista: {count}")
