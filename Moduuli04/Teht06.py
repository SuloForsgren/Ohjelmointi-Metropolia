import random 

pisteet = int(input("Anna arvottavien pisteiden määrä: "))
kohta = 1
alueella = 0

while kohta <= pisteet :
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1: 
        alueella += 1

    kohta += 1

pi_arvo = 4 * alueella / pisteet 
print(pi_arvo)