lista = []

while True: 
    luku = input("Anna luku: ")

    if luku == "" :
        break

    else :
        luku = int(luku)
        lista.append(luku)
        print(luku)

lista = sorted(lista)
print(f"Pienin luku on {lista[0]} ja suurin luku on {lista[-1]}")