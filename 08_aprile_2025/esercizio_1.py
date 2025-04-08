
# if è_palindroma(frase):
#     print("È palindroma!")
# else:
#     print("Non è palindroma.")
#caratteri_validi = "abcdefghijklmnopqrstuvwxyz"   # Solo lettere, niente numeri

# def è_valido(c):
#     return c in caratteri_validi

def pulisci_testo(testo):
    return ''.join(filter(str.isalpha, testo.lower())) # oppure è_valido(c) con alfabeto di caratteri_validi

def è_palindroma(testo):
    testo_pulito = pulisci_testo(testo); return testo_pulito == testo_pulito[::-1] #reverse
frase = input("Inserisci una parola o una frase: ")    


print("È palindroma!" if è_palindroma(frase) else "Non è palindroma.") #if ternario




