def vuodenaika(vuodenajat, kuukausi) :
    if kuukausi == 0 :
        return "Virheellinen kuukausi"
    elif kuukausi == 12 or kuukausi <= 2 :
        return vuodenajat[0]
    elif kuukausi <= 5 :
        return vuodenajat[1]
    elif kuukausi <= 8 :
        return vuodenajat[2]
    elif kuukausi <= 11 :
        return vuodenajat[3]
    else : 
        return "Virheellinen kuukausi"

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
kk = int(input("Anna kuukausi lukuna: "))
print(vuodenaika(vuodenajat, kk))