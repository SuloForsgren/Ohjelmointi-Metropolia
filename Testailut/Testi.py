kohta = 0
lista = ["eka", "toinen", "kolmas"]

nimi = input("Anna Nimesi:")

for i in lista :
    print(lista[kohta])
    kohta += 1
    print("Rivi Valmis!\n")

print(f"Ohjelma valmis! Hei {nimi}!")