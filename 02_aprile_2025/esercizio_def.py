def crea_lista(numero_elementi):
    lista = []
    for _ in range(numero_elementi):
        numero = int(input(f"Inserisci il numero: "))
        lista.append(numero)
    return lista

def quadrato(numero):
    return numero ** 2

def somma_lista(lista):
    somma = 0
    for num in lista:
        somma += num
    return somma

# Creazione di più liste con numeri inseriti dall'utente
numero_liste = int(input("Quante liste vuoi creare? "))
liste_numeri = []
for i in range(numero_liste):
    numero_elementi = int(input(f"Quanti elementi vuoi inserire nella lista"))
    lista = crea_lista(numero_elementi)
    liste_numeri.append(lista)

# Calcolo dei quadrati per ciascuna lista
liste_quadrati = []
for lista in liste_numeri:
    lista_quadrati = []
    for num in lista:
        lista_quadrati.append(quadrato(num))
    liste_quadrati.append(lista_quadrati)

# Creazione di un'unica lista somma
lista_somma = []
for lista in liste_quadrati:
    lista_somma.append(somma_lista(lista))

# Stampa dei risultati
for i, lista in enumerate(liste_numeri):
    print(f"La lista {i + 1} inserita è:", lista)
    print(f"I quadrati dei numeri della lista {i + 1} sono:", liste_quadrati[i])
print("La lista delle somme dei quadrati è:", lista_somma)

somma = 0
for var in lista_somma:
    somma = somma + var
print("La somma delle somme è:", somma)
    
