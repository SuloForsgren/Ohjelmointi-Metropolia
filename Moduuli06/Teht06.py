#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
#sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan 
#yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan 
#halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle 
#(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def pizza(ekahalk, ekahint) :

    cm2 = math.pi * ((ekahalk / 2) ** 2)
    laskettu = ekahint / cm2
    return laskettu


p1halkaisija = float(input("Anna pizzan halkaisija: "))
p1hinta = float(input("Pizzan hinta euroina: "))
#p2halkaisija = float(input("Anna pizzan halkaisija: "))
#p2hinta = float(input("Pizzan hinta euroina: "))

palautus = pizza(p1halkaisija, p1hinta)
print(palautus)