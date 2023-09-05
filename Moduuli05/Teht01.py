import random
nopat = int(input("Monta noppaa heitetään?: "))
lista = []

for i in range(0, nopat) :
    heitto = random.randint(1,6)
    lista.append(heitto)
print(sum(lista))   