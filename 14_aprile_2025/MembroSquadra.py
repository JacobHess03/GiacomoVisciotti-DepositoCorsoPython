class MembroSquadra:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
        
    def descrivi(self):
        print(f"Il membro della squadra è: ")

class Giocatore(MembroSquadra):
    
    def __init__(self, nome, età, ruolo, num_maglia, rate):
        
        super().__init__(nome, età)
        self.ruolo = ruolo
        self.num_maglia = num_maglia
        self.rate = rate
        
    def gioca_partita(self):
        
        match self.ruolo:
            case "Attaccante":
                print("Il giocatore sta tirando in porta.")
                
            case "Difensore":
                print("Il giocatore sta difendendo l'area.")
            
            case "Centrocampista":
                print("Il giocatore sta gestendo il gioco.")
                
            case "Portiere":
                 print("Il giocatore sta parando un tiro.")


class Allenatore(MembroSquadra):
    
    def __init__(self, nome, età, rate, esperienza):
        
        super().__init__(nome, età)
        self.rate = rate
        self.esperienza = esperienza
        
    def dirigi_allenamento(self):
        
        if self.rate < 0.5:
            print("Diretto in maniera difensiva.")
        elif self.rate > 0.5:
            print("Diretto in maniera offensiva.")
        

                
class Assistente(MembroSquadra):
    
    def __init__(self, nome, età, esperienza, rate):
        
        super().__init__(nome, età)
        self.esperienza = esperienza
        self.rate = rate
        
    def supporta_team(self):
        
        print("Contribuisce al supporto della squadra.")
        
class Fisioterapista(Assistente):
    
    def __init__(self, nome, età, esperienza, rate, titolo):
    
        super().__init__(nome, età)
        self.esperienza = esperienza
        self.rate = rate
        self.titolo = titolo
        
    def supporta_team(self):
        super().supporta_team()
        print(f"Grazie al suo titolo {self.titolo} ed i suoi anni di esperienza {self.esperienza}.")
        
class AnalistaDiGioco(Assistente):
    
    def __init__(self, nome, età, esperienza, rate, titolo, storico):
    
        super().__init__(nome, età)
        self.esperienza = esperienza
        self.titolo = titolo
        self.storico = storico
        self.rate = rate + storico
        
    def supporta_team(self):
        super().supporta_team()
        print(f"Grazie al suo titolo {self.titolo} ed i suoi anni di esperienza {self.esperienza}.")
        
        
        
    
        
        
        
    
    
        

            
                
                


        
