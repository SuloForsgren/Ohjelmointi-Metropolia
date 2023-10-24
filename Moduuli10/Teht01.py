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
        siirtymä = self.kerros

        print(kerros)
        if (tavoite - kerros) > 0:
            for i in range(tavoite - siirtymä) :
                siirtymä = Hissi.kerros_ylös(siirtymä)
                if siirtymä > self.ylin :
                    siirtymä = self.ylin
                    break
                print(siirtymä)
            

        elif (tavoite - kerros) < 0:
            for i in range(siirtymä - tavoite) :
                siirtymä = Hissi.kerros_alas(siirtymä)
                if siirtymä < self.alin :
                    siirtymä = self.alin
                    break
                print(siirtymä)
            
        self.kerros = siirtymä
        print("-------")
        


h = Hissi(1,15)
h.siirry_kerrokseen(7)
h.siirry_kerrokseen(4)
h.siirry_kerrokseen(32)
h.siirry_kerrokseen(-8)