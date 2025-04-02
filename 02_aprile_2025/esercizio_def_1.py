def crea_lista():
    flag = True
    lista = []
    while(flag):
        numero = int(input(f"Inserisci il numero"))
        lista.append(numero)
        risposta = input("Vuoi inserire un altro numero? (s/n): ")
        if risposta.lower() == 'no':
            flag = False
    return lista

def quadrato(numero):

    return numero ** 2

def somma_lista(lista):
   
    somma = 0
    for num in lista:
        somma += num
    return somma

# Creazione della lista con numeri inseriti dall'utente
lista_numeri = crea_lista()
print("La lista inserita è:", lista_numeri)

# Calcolo del quadrato per ciascun numero e creazione di una nuova lista
lista_quadrati = []
for num in lista_numeri:
    lista_quadrati.append(quadrato(num))
print("I quadrati dei numeri sono:", lista_quadrati)

# Calcolo della somma degli elementi della lista originale
somma = somma_lista(lista_quadrati)
print("La somma degli elementi della lista è:", somma)
