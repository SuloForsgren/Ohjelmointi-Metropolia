import random

def heitto(max) :
    heitot = 0
    while True: 
        luku = random.randint(1,max)
        heitot += 1

        print(luku)
        if (luku == max) :
            break
        

maksimi = int(input("Anna luku: "))
heitto(maksimi)