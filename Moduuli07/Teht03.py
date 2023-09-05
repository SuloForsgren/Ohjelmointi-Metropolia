def hae() :
    return "Haetaan!"

def tallenna(sanakirja) :
    icao = int(input("Anna ICAO koodi: "))
    lnimi = (input("Anna lentokentälle nimi: "))
    sanakirja = {icao:lnimi}

    return sanakirja

sanakirja = {}
while True:
    valikko = int(input("Syöte numeroarvoinen! Haluatko hakea(1), tallentaa(2) vai lopettaa(3)?: "))
    if valikko == 1 :
        print(hae(sanakirja))

    elif valikko == 2 :
        print(tallenna(sanakirja))

    else :
        print(sanakirja)
        break