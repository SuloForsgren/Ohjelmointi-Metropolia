#Määritetään muuttuja "ysade" käyttäjän syötteestä
ysade = input("Anna ympyrän säde: ")

#Muutetaan int muotoon
ysade = int(ysade)

#Lasketaan tulos
tulos = 3.14 * (ysade * ysade)

#Tulostetaan
print(f"Tulos: {tulos}")