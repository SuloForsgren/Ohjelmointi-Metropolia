class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, th_nopeus = 0, matka = 0) :
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.th_nopeus = th_nopeus
        self.matka = matka

auto = Auto("ABC-123", 142)

print(
f"""
Rekkari: {auto.rekisteritunnus}
Huippunopeus: {auto.huippunopeus}km/h
Tämänhetkinen nopeus: {auto.th_nopeus}
Auton kulkema matka: {auto.matka}
""")