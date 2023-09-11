
def lisaa_Lentokentta(Lentokentät) :
    lkNimi = input("Anna lentoaseman nimi: ")
    icao = input("Anna lentoaseman ICAO koodi: ")
    Lentokentät[icao] = lkNimi
    return Lentokentät

def hae_Lentokentta(Lentokentät) :
    haetaan_ICAO_koodilla = input("Hae ICAO koodilla lentoasemaa: ")
    for i in Lentokentät :
        if haetaan_ICAO_koodilla in Lentokentät :
            return Lentokentät[haetaan_ICAO_koodilla]
        else :
            return "Virheellinen ICAO Koodi!"
        
Lentokentät = {}
print("Syötä numero -- 1, Syöttääksesi tietoja sanakirjaan")
print("Syötä numero -- 2 hakeaksesi tietoja sanakirjasta ICAO koodilla")
print("Syötä numero -- 3 lopettaaksesi ohjelman suorituksen")
print()
syote = int(input("Anna numero 1-3: "))

while syote != 3 :
    
    if syote == 1 :
        print(lisaa_Lentokentta(Lentokentät))

    elif syote == 2 :
        print(hae_Lentokentta(Lentokentät))
    
    print("Syötä numero -- 1, Syöttääksesi tietoja sanakirjaan")
    print("Syötä numero -- 2 hakeaksesi tietoja sanakirjasta ICAO koodilla")
    print("Syötä numero -- 3 lopettaaksesi ohjelman suorituksen")
    print()
    syote = int(input("Anna numero 1-3: "))

print("Lopetettiin, Heippa!")     