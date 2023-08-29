#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
#Ohjelma palauttaa listassa olevien lukujen summan. 
#Kirjoita testausta varten pääohjelma, jossa luot listan, 
#kutsut funktiota ja tulostat sen palauttaman summan.

def luvut(lista) :
    return sum(lista)


kokonaisluvut = [2,5,1,23,8,5,3,2]
palautus = luvut(kokonaisluvut) 
print(palautus)