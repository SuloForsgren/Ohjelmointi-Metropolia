pituus = int(input("Anna kuhan pituus sentteinä: "))

if pituus < 37 :
    alle = 37 - pituus
    if alle == 1 :
        print(f"Laske Kuha takaisin!\nKuhasi on alimittainen {alle} sentin!")
    else :
        print(f"Laske Kuha takaisin!\nKuhasi on alimittainen {alle} senttiä!")

else :
    print(f"{pituus} senttiä")