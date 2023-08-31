#Määritellään muuttujat
luku1 = int(input("Luku1: "))
luku2 = int(input("Luku2: "))
luku3 = int(input("Luku3: "))


#Luodaan muuttujat eri vastauksille ja suoritetaan laskutoimitukset
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3
#keskiarvo = round(keskiarvo, 2)
#Tulostetaan vastaukset
print(f"Summa on: {summa}")
print(f"tulo on: {tulo}")
print(f"keskiarvo on: {keskiarvo}")