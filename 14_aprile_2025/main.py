import MembroSquadra as MS
import random


squadra_1 = []
squadra_2 = []

def inserisci_giocatore():
    squadra = []
    for i in range(5):
        print(f"Giocatore {i}")
        nome = input("Inserisci il nome: ")
        età = int(input("Inserisci l'età: "))
        ruolo = input("Inserisci il ruolo: ")
        num_maglia = int(input("Inserisci il numero di maglia: "))
        rate = float(input("Inserisci il rate: "))
        G1 = MS.Giocatore(nome, età, ruolo, num_maglia, rate)
        squadra.append(G1)
    return squadra

def inserisci_allenatore(nome, età, rate, esperienza):
    nome = input("Inserisci il nome: ")
    età = int(input("Inserisci l'età: "))
   
    esperienza = int(input("Inserisci il numero di anni di esperienza: "))
    rate = float(input("Inserisci il rate: "))
   
    A1 = MS.Allenatore(nome, età, rate, esperienza)
    return A1

def inserisci_fisioterapista(nome, età, esperienza, rate, titolo):
    nome = input("Inserisci il nome: ")
    età = int(input("Inserisci l'età: "))
   
    esperienza = int(input("Inserisci il numero di anni di esperienza: "))
    rate = float(input("Inserisci il rate: "))
    titolo = input("Inserisci il titolo: ")
    F1 = MS.Fisioterapista(nome, età, esperienza, rate, titolo)
    return F1

def inserisci_analista(nome, età, esperienza, rate, titolo, storico):
    nome = input("Inserisci il nome: ")
    età = int(input("Inserisci l'età: "))
   
    esperienza = int(input("Inserisci il numero di anni di esperienza: "))
    rate = float(input("Inserisci il numero di maglia: "))
    titolo = input("Inserisci il titolo: ")
    storico = float(input("Inserisci lo storico: "))
    A1 = MS.AnalistaDiGioco(nome, età, esperienza, rate, titolo, storico)
    return A1


# def gioca_partita(squadra_1, squadra_2):
    
#     rate_1 = 0
#     rate_2 = 0
#     for player in squadra_1:
#         rate_1 = player.rate + rate_1
#     for player in squadra_2:
#         rate_2 = player.rate + rate_2
#     differenza = abs(rate_1 - rate_2)
    
#     if rate_1 > rate_2:
#         print("Ha vinto la prima squadra.")
#     else:
#         print("Ha vinto la seconda squadra.")


def gioca_partita(squadra1,squadra2):


    for i in range(len(squadra1)):

        sum=sum+squadra1[i].rate

    for i in range(len(squadra2)):

        sum1=sum1+squadra2[i].rate


    if(sum>sum1):

        print("squadra1 ha vinto")

        a=0
        b=0


        while(a<=b):
            a=random.randint(1,6)
            b=random.randint(1,5)


        print(f" squdra 1 {a}--- squadra2 {b}")



    elif(sum<sum1):

        print("squadra 2 ha vinto")


        a=0
        b=0


        while(a>=b):
            a=random.randint(1,6)
            b=random.randint(1,5)


        print(f" squdra 1 {a}--- squadra2 {b}")

    else:
        print("pareggio")


        a=1
        b=0


        while(a<b) or (a>b):
            a=random.randint(1,6)
            b=random.randint(1,5)


        print(f" squdra 1 {a}--- squadra2 {b}")
    

flag = True
while(flag):
    scelta = int(input("Inserisci \n1.Giocatori per la squadra\n2.Allenatore \n3.Fisioterapista \n4.Analista di gioco"))
    match scelta:
        case 1:
            
            print("Inserisci per la prima squadra.")
            squadra_1 = inserisci_giocatore()
            print("Inserisci per la seconda squadra.")
            squadra_2 = inserisci_giocatore()
        case 2:
            print("Inserisci allenatore per la prima squadra.")
            squadra_1.append(inserisci_allenatore())
            print("Inserisci allenatore per la seconda squadra.")
            squadra_2.append(inserisci_allenatore())
            
        case 3:
            print("Inserisci il fisioterapista per la prima squadra.")
            squadra_1.append(inserisci_fisioterapista())
            print("Inserisci il fisioterapista per la seconda squadra.")
            squadra_2.append(inserisci_fisioterapista())
            
        case 4: 
            print("Inserisci l'analista per la prima squadra.")
            squadra_1.append(inserisci_analista())
            print("Inserisci l'analista per la seconda squadra.")
            squadra_2.append(inserisci_analista())
flag = False
    
gioca_partita(squadra_1, squadra_2)           
            
            
            
    
    