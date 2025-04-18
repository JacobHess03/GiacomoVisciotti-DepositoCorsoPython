from abc import ABC, abstractmethod
from math import pi, sqrt

class Forma(ABC):
    """
    Classe astratta per le forme geometriche.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cerchio(Forma):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimetro(self):
        return 2 * pi * self.r

class Rettangolo(Forma):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

    def perimetro(self):
        return 2 * (self.b + self.h)

class Triangolo(Forma):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimetro() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

def forma_massima(lista_forme, criterio):
    """
    Restituisce la forma con il valore massimo tra area o perimetro.
    """
    massimo = 0
    forma_max = None
    for f in lista_forme:
        if criterio == 'area':
            valore = f.area()
        elif criterio == 'perimetro':
            valore = f.perimetro()
        else:
            print("Criterio non valido.")
            return None

        if valore > massimo:
            massimo = valore
            forma_max = f

    return forma_max

def menu():
    forme = [
        Cerchio(3),
        Rettangolo(4, 2),
        Triangolo(3, 4, 5),
        Cerchio(2)
    ]

    while True:
        print("\n--- Menu Forme Geometriche ---")
        print("1. Crea nuova forma")
        print("2. Visualizza tutte le forme")
        print("3. Forma con area massima")
        print("4. Forma con perimetro massimo")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case '1':
                tipo = input("Tipo (cerchio/rettangolo/triangolo): ").lower()
                if tipo == 'cerchio':
                    r = float(input("Inserisci raggio: "))
                    forme.append(Cerchio(r))
                elif tipo == 'rettangolo':
                    b = float(input("Base: "))
                    h = float(input("Altezza: "))
                    forme.append(Rettangolo(b, h))
                elif tipo == 'triangolo':
                    a = float(input("Lato a: "))
                    b = float(input("Lato b: "))
                    c = float(input("Lato c: "))
                    forme.append(Triangolo(a, b, c))
                else:
                    print("Tipo non valido.")

            case '2':
                indice = 1
                for f in forme:
                    tipo = type(f).__name__
                    print(f"{indice}. {tipo} - Area: {f.area():.2f}, Perimetro: {f.perimetro():.2f}")
                    indice += 1

            case '3':
                fmax = forma_massima(forme, 'area')
                if fmax:
                    print("Forma con area massima:", type(fmax).__name__, "Area:", round(fmax.area(), 2))

            case '4':
                fmax = forma_massima(forme, 'perimetro')
                if fmax:
                    print("Forma con perimetro massimo:", type(fmax).__name__, "Perimetro:", round(fmax.perimetro(), 2))

            case '5':
                print("Uscita in corso...")
                break

            case _:
                print("Opzione non valida.")

if __name__ == '__main__':
    menu()
