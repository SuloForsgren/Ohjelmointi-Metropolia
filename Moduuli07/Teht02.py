def nimet (syote, nimilista) :
    
    print(nimilista)
    for j in nimilista :
        if j in nimilista :
           return "Aiemmin syötetty nimi"
        else :
           nimilista.add(syote)
           return "Uusi nimi"

def tarkistus(lista) :
     for i in lista:
          print(i)



nimilista = set
while True :
    nimi = input("Anna nimi: ")
    if nimi != "" :
        print(f"{nimet(nimi, nimilista)}")
    else : 
        break

tarkistus(nimilista)