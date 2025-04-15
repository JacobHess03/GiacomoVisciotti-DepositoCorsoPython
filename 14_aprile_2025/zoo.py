class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self):
        print("Fa un suono")

class Leone(Animale):
    def __init__(self, nome, eta, tipo, lun_artigli):
        super().__init__(nome, eta)
        self.tipo = tipo
        self.lun_artigli = lun_artigli
    
    def fai_suono(self):
        super().fai_suono()
        print("GRR")
    
    def metodo_caccia(self):
        print("Il leone si abbassa per poi cacciare.")
    
    def mostra_artigli(self):
        print("Lunghezza degli artigli:", self.lun_artigli)

class Giraffa(Animale):
    def __init__(self, nome, eta, tipo, lun_collo):
        super().__init__(nome, eta)
        self.tipo = tipo
        self.lun_collo = lun_collo
    
    def fai_suono(self):
        super().fai_suono()
        print("BEE")
    
    def mostra_collo(self):
        print(f"La lunghezza del collo: {self.lun_collo}")

class Pinguino(Animale):
    def __init__(self, nome, eta, tipo, v_water, lun_pinne):
        super().__init__(nome, eta)
        self.tipo = tipo
        self.v_water = v_water
        self.lun_pinne = lun_pinne
    
    def fai_suono(self):
        super().fai_suono()
        print("AHH")
    
    def mostra_velocita(self):
        print(f"Velocità in acqua: {self.v_water}")
    
    def mostra_pinne(self):
        print(f"Lunghezza pinne: {self.lun_pinne}")
