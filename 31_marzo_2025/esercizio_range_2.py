
flag = True
while (flag):
    num_1 = int(input("Inserisci il primo numero dell'intervallo: "))
    num_2 = int(input("Inserisci il secondo numero dell'intervallo: "))

        #creo liste vuote
    primi = []
    non_primi = []

    for num in range(num_1, num_2 + 1):
        #verifico il caso dell'uno
        if num < 2:
            non_primi.append(num)
        else:
            primo = True
            #Verifico che il numero sia primo
            for i in range(2, num - 1):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                #se è primo lo aggiungo alla lista dei numeri primi
                primi.append(num)
            else:
                #se non è primo lo aggiungo alla lista dei numeri non primi
                non_primi.append(num)

    scelta = input("Vuoi vedere i numeri primi (1), non primi (2) o entrambi (3)? ")

    if scelta == '1':
        print("Numeri primi nell'intervallo:", primi)
    elif scelta == '2':
        print("Numeri non primi nell'intervallo:", non_primi)
    elif scelta == '3':
        print("Numeri primi:", primi)
        print("Numeri non primi:", non_primi)
    else:
        print("Scelta non valida.")

    scelta_finale = input("Vuoi ripetere? (s/n)")
    if scelta_finale.lower() == "no":
        flag = False