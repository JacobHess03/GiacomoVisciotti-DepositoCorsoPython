
insieme = 0
while (insieme < 5):


    num = int(input("Inserisci un numero: "))

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Non è un numero primo.")
                
            else:
                print("È un numero primo.")
                insieme += 1
    else:
        print("Non è un numero primo.")