from random import randint

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

autot = []
maali = False
for luku in range(1,11) :
    hnopeus = randint(100,200)
    auto = Auto(f"ABC-{luku}", hnopeus)
    autot.append(auto)

while maali != True:
    for auto in autot :
        auto.kiihdytä(randint(-10,15))
        auto.kulje(1)
        if auto.matka >= 10000 :
            maali = True
    
for auto in autot :
    print(f"""
    =========================================
    |Rekkari: {auto.rekisteritunnus}        
    |Huippunopeus: {auto.huippunopeus}km/h  
    |Tämänhetkinen nopeus: {auto.nopeus}km/h
    |Kuljettu matka: {auto.matka}km         
    =========================================
    """)