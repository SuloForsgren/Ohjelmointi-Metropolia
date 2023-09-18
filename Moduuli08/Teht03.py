import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Ruutt!',
         autocommit=True
         )

def haeLentoasemaEtaisyys(koodi1, koodi2, saadut_koordinaatit):
    sql = "SELECT latitude_deg, longitude_deg FROM airport where ident IN (%s, %s)"

    kursori = yhteys.cursor()
    kursori.execute(sql, (koodi1, koodi2))
    haku = kursori.fetchall()

    for rivi in haku:
        saadut_koordinaatit.append(rivi)


    return saadut_koordinaatit

saadut_koordinaatit = []
koodi1 = input("Anna ensimmäinen ICAO koodi: ")
koodi2 = input("Anna toinen ICAO koodi: ")

koodit = haeLentoasemaEtaisyys(koodi1, koodi2, saadut_koordinaatit)
print(f"Lentokettien välissä on matkaa noin {int(distance.distance(koodit[0], koodit[1]).km)} kilometriä.")