#Definisco la funzione
def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return[0]
    elif num == 2:
        return [0, 1]
    
    seq = [0,1]
    #ciclo per la sequenza di fibonacci
    for i in range(2, num):
        seq.append(seq[i-1] + seq[i-2])
    return seq

num_ins = int(input("Inserisci un numero: "))
sequenza = fibonacci(num_ins)
print("La sequenza è", num_ins, "è", sequenza)