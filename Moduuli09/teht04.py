from random import randint

class Kilpa_Autot():
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus    
        self.nopeus = nopeus
        self.matka = matka
        
    def kiihdytä(self, muutos):
        print(muutos)


autot = []
for luku in range(1,11) :
    hnopeus = randint(100,200)
    auto = Kilpa_Autot(f"ABC-{luku}", hnopeus)
    autot.append(auto)


for i in autot :
    auto.kiihdytä(randint(-10,15))