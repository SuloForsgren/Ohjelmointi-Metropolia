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
                print(siirtymä)
        
        elif (tavoite - kerros) < 0:
            for i in range(siirtymä - tavoite) :
                siirtymä = Hissi.kerros_alas(siirtymä)
                print(siirtymä)
        
        self.kerros = siirtymä
        print("-------")
        


h = Hissi(1,50)
h.siirry_kerrokseen(7)
h.siirry_kerrokseen(4)
h.siirry_kerrokseen(33)
h.siirry_kerrokseen(2)