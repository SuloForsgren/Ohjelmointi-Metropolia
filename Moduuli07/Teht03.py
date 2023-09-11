
def lisaa_Lentokentta(Lentokentät) :
    lkNimi = input("Anna lentokentän nimi: ")
    icao = input("Anna lentokentän ICAO koodi: ")
    Lentokentät[lkNimi] = icao
    return Lentokentät

def hae_Lentokentta() :
    return "Haettu"

Lentokentät = {}

syote = int(input("1, Syöttääksesi, 2 hakeaksesi ja 3 lopettaaksesi: "))

while syote != 3 :
    
    if syote == 1 :
        print(lisaa_Lentokentta(Lentokentät))
    elif syote == 2 :
        print(hae_Lentokentta())
    syote = int(input("1, Syöttääksesi, 2 hakeaksesi ja 3 lopettaaksesi: "))

print("Lopetettiin, Heippa!")