class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus    
        self.nopeus = nopeus
        self.matka = matka
        
    def kiihdytä(self, muutos):

        if muutos < 0 :
            self.nopeus += muutos
            if self.nopeus < 0 :
                self.nopeus = 0
                
        elif muutos > 0 :
            self.nopeus += muutos
            if self.nopeus > self.huippunopeus :
                self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku, nopeus = 0, matka = 0):
        self.akku = akku
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensa, nopeus = 0, matka = 0):
        self.bensa = bensa
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(104)
polttomoottoriauto.kiihdytä(79)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton mittarin lukema: {sahkoauto.matka}")
print(f"Polttomoottoriauton mittarin lukema: {polttomoottoriauto.matka}")