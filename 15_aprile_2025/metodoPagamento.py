class MetodoPagamento:
    def __init__(self, iban, codice, saldo):
        self.__iban = iban
        self.__saldo = saldo
    
    
    
    def get_saldo(self):
        return self.__saldo()
        
    def effetua_pagamento(self, importo):
        self.__saldo -= importo
        
class CartaDiCredito(MetodoPagamento):
    def __init__(self, iban, saldo, codice):
        self.__codice = codice
        super().__init__(iban, saldo)
        
    def effetua_pagamento(self, importo, codice):
        if self.__codice == codice:
            self.__saldo -= importo
        else:
            print("Codice non valido.")
        
    
    
class PayPal(MetodoPagamento):
    
    def __init__(self, iban, saldo, email, password):
        self.__email = email
        self.__password = password
        super().__init__(iban, saldo)
        
    def effetua_pagamento(self, importo, email, password):
        if self.__email == email and self.__password == password:
            self.__saldo -= importo
        else:
            print("Credenziali non valide.")
            
class BonificoBancario(MetodoPagamento):
    
    def __init__(self, iban, saldo, codice, password):
        
        self.__codice = codice
        self.__password = password
        super().__init__(iban, saldo)
        
    def effetua_pagamento(self, importo, codice, password):
        if self.__codice == codice and self.__password == password:
            self.__saldo -= importo
        else:
            print("Credenziali non valide.")   
    
        
    
class GestorePagamenti:
    def __init__(self):
        self.__metodi = []

    def aggiungi_metodo(self, metodo):
        if type(metodo).__name__ in ["CartaDiCredito", "PayPal", "BonificoBancario"]:
            self.__metodi.append(metodo)
        else:
            print("Metodo di pagamento non valido.")

    def mostra_metodi(self):
        if not self.__metodi:
            print("Nessun metodo di pagamento registrato.")
        else:
            for i, metodo in enumerate(self.__metodi, 1):
                print(f"{i}. {type(metodo).__name__}")

    def paga(self, indice, importo, *credenziali):
        if 0 <= indice < len(self.__metodi):
            metodo = self.__metodi[indice]
            try:
                metodo.effetua_pagamento(importo, *credenziali)
            except TypeError:
                print("Errore: credenziali insufficienti o errate.")
        else:
            print("Indice metodo di pagamento non valido.")

    
        
        
        
        
        
        
        