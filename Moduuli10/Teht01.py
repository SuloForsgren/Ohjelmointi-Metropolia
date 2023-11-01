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
                if kerros > self.ylin :
                    kerros = self.ylin
                    break
                print(kerros)
            

        elif (tavoite - kerros) < 0:
            for i in range(kerros - tavoite) :
                kerros = Hissi.kerros_alas(kerros)
                if kerros < self.alin :
                    kerros = self.alin
                    break
                print(kerros)
            
        self.kerros = kerros
        print("-------")
        


h = Hissi(1,15)
h.siirry_kerrokseen(7)
h.siirry_kerrokseen(4)
h.siirry_kerrokseen(32)
h.siirry_kerrokseen(-8)