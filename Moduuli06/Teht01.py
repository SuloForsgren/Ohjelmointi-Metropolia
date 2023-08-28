import random

def heitto() :
    heitot = 0
    while True: 
        luku = random.randint(1,6)
        heitot += 1

        print(luku)
        if (luku == 6) :
            break
        
heitto()