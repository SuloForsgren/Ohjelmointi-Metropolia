class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = self.alin

    def kerros_ylös(kerros):
        kerros += 1
        return kerros
        


    def kerros_alas(kerros):
        kerros -= 1
        return kerros

    def siirry_kerrokseen(self, tavoite):
        self.tavoite = tavoite
        kerros = self.kerros


        print(kerros)
        if (tavoite - kerros) > 0:
            for i in range(tavoite - kerros) :
                kerros = Hissi.kerros_ylös(kerros)
                print(kerros)
        
        elif (tavoite - kerros) < 0:
            for i in range(kerros - tavoite) :
                kerros = Hissi.kerros_alas(kerros)
                print(kerros)


        self.kerros = kerros
        print("-------")
        
class Talo:
    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissilista = []
        
        for i in range(hissit) :
            self.hissilista.append(Hissi(self.alin, self.ylin))

    def aja_hissiä(self, hnumero, kohde):
        self.hissilista[hnumero].siirry_kerrokseen(kohde)

    def palohälytys(self):
        for i in self.hissilista :
            i.siirry_kerrokseen(self.alin)

#h = Hissi(1,15)
#h.siirry_kerrokseen(7)
#h.siirry_kerrokseen(4)
#h.siirry_kerrokseen(15)
#h.siirry_kerrokseen(2)

talo = Talo(1,24,3)
talo.aja_hissiä(0,22) #Hissi 1
talo.aja_hissiä(2,12) #Hissi 3
talo.aja_hissiä(1,4)  #Hissi 2
print(f"Hissi 1: kerros {talo.hissilista[0].tavoite} \nHissi 2: kerros {talo.hissilista[1].tavoite} \nHissi 3: kerros {talo.hissilista[2].tavoite}")

talo.palohälytys()
print(f"Hissi 1: kerros {talo.hissilista[0].tavoite} \nHissi 2: kerros {talo.hissilista[1].tavoite} \nHissi 3: kerros {talo.hissilista[2].tavoite}")