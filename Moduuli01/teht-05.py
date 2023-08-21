#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

luoti = 13.3
naula = 13.3 * 32
leiviska = naula * 20

ileiviskat = float(input("Leiviskät: "))
inaulat = float(input("Naulat: "))
iluodit = float(input("Luodit: "))

luodit = iluodit * luoti
naulat = inaulat * naula
leiviskat = ileiviskat * leiviska
yht = luodit + naulat + leiviskat

kilot = yht / 1000
kilot = int(kilot)
grammat = yht % 1000
grammat = round(grammat, 2)
print(f"{kilot} kilogrammaa ja {grammat} grammaa.")