from random import randint

class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus    
        self.nopeus = nopeus
        self.matka = matka
        
    def kiihdytä(self, muutos):
        if muutos < 0:
            self.nopeus += muutos
            if self.nopeus < 0:
                self.nopeus = 0
        elif muutos > 0:
            self.nopeus += muutos
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Kilpailu():
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"""
            =========================================
            |Rekkari: {auto.rekisteritunnus}        
            |Huippunopeus: {auto.huippunopeus}km/h  
            |Tämänhetkinen nopeus: {auto.nopeus}km/h
            |Kuljettu matka: {auto.matka}km         
            =========================================
            """)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrit:
                return True
        return False

autot = []
for luku in range(1, 11):
    hnopeus = randint(100, 200)
    auto = Auto(f"ABC-{luku}", hnopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if tunnit == 10:
        kilpailu.tulosta_tilanne()
    tunnit += 1

    if tunnit > 10:
        tunnit = 0
kilpailu.tulosta_tilanne()