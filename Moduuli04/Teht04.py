import random

luku = random.randint(1,10)
while True :

    arvaus = int(input("Arvaa luku: "))

    if arvaus == luku :
        print("Oikein!")
        break
    elif luku < arvaus :
        print("Liian suuri arvaus!")
    
    elif luku > arvaus : 
        print("Liian pieni arvaus")