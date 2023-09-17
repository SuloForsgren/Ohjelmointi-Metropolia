import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Ruutt!',
         autocommit=True
         )

def hae_ICAO_Koodilla_lentoaseman_nimi(ICAO_koodi):
    sqlQuery = f"SELECT airport.name, airport.municipality FROM airport WHERE airport.ident = '{ICAO_koodi}';"
    kursori = yhteys.cursor()
    kursori.execute(sqlQuery)
    tulos = kursori.fetchall()

    return tulos

ICAO_koodi = input("Syötä ICAO koodi: ")

palautus = hae_ICAO_Koodilla_lentoaseman_nimi(ICAO_koodi)
print(palautus)
print(f"ICAO-Koodilla {ICAO_koodi} löytyy lentokenttä {palautus[0][0]} ja sijainti on {palautus[0][1]}")