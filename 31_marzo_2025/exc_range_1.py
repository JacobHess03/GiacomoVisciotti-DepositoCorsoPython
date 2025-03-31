flag = True
while(flag):
    scelta = input("Vuoi inserire un numero o una stringa? (Numero), (Stringa)")
    if scelta.lower() == "numero":
        num = int(input("Inserisci il numero: "))
        if num % 2 == 0:
            print("Pari")
        else:
            print("Dispari")
    elif scelta.lower() == "stringa":
        nome = input("Inserisci un nome: ")
        for count in range(len(nome)):
            count += 1
            
        if count % 2 == 0:
            print("Pari: ", count)
        else:
            print("Dispari: ", count)

    scelta_2 = input("Vuoi ripetere?")
    if scelta_2.lower() == "no":
        flag = False
    else:
        flag = True


