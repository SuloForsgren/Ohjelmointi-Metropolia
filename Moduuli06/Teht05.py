#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen 
#kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
#Kirjoita testausta varten pääohjelma, jossa luot listan, 
#kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def luvut(lista) :
    muokattava = []
    for luku in lista :
        if luku % 2 == 0 :
            muokattava.append(luku)


    return muokattava

kokonaisluvut = [2, 3, 4, 15, 5, 7, 13, 213]
palautus = luvut(kokonaisluvut) 
print(palautus)