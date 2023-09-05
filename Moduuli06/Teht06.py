import math

def pizza1(ekahalk, ekahint) :

    cm2 = math.pi / 4 * ekahalk ** 2
    laskettu = ekahint / (cm2 / 10000)
    return laskettu

def pizza2(tokahalkaisija, tokahint) :

    cm2 = math.pi / 4 * tokahalkaisija ** 2
    laskettu = tokahint / (cm2 / 10000)
    return laskettu


p1halkaisija = float(input("Anna pizzan halkaisija: "))
p1hinta = float(input("Pizzan hinta euroina: "))
p2halkaisija = float(input("Anna pizzan halkaisija: "))
p2hinta = float(input("Pizzan hinta euroina: "))

palautus = pizza1(p1halkaisija, p1hinta)
palautus2 = pizza2(p2halkaisija, p2hinta)

if palautus < palautus2 :
    print("Ensimmäinen pizza on halvempi!")
else:
    print("Toinen pizza on halvempi!")

print(palautus)