def nimet (syote, nimilista) :
    
    #print(nimilista)
    if syote in nimilista :
        return "Aiemmin syötetty nimi"
    else :
        nimilista.add(syote)
        return "Uusi nimi"

def tarkistus(lista) :
     for i in lista:
          print(i)



nimilista = set()
arvo = True
while arvo :
    nimi = input("Anna nimi: ")
    if nimi != "" :
        print(nimet(nimi, nimilista))
    else : 
        arvo = False

tarkistus(nimilista)