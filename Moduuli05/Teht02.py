lista = []

while True:
    luku = input("Anna luku: ")

    if luku == "" :
        break

    luku = int(luku)
    lista.append(luku)

pituus = len(lista)
lista.sort(reverse=True)
if pituus < 5 :
    print(lista[0:pituus])
else :
    print(lista[0:5])