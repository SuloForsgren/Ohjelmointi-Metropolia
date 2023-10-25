class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0) :
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
        self.matka = self.nopeus * tunnit


auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"{auto.nopeus} km/h")

auto.kulje(1.5)
auto.kulje(3)
print(f"{auto.matka} metriä")

auto.kiihdytä(-200)
print(f"{auto.nopeus} km/h")