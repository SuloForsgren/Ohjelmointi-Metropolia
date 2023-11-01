class Julkaisu:
    def __init__(self, nimi) :
        self.nimi = nimi
    
class Kirja(Julkaisu):
    
    def __init__(self, nimi, kirjoittaja, sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan nimi --> {self.nimi}. Kirjan kirjoittaja --> {self.kirjoittaja}. Kirjan sivumäärä --> {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi --> {self.nimi}. Kirjan päätoimittaja --> {self.paatoimittaja}")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()