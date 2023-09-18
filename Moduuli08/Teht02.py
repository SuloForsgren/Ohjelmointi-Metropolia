import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Ruutt!',
         autocommit=True
         )

def hae_maakoodilla_lentoasemat(maaKoodi):
    sqlQuery = f"SELECT airport.type, count(airport.name) FROm airport WHERE iso_country = '{maaKoodi}' GROUP BY airport.type;"
    kursori = yhteys.cursor()
    kursori.execute(sqlQuery)
    tulos = kursori.fetchall()

    return tulos

maaKoodi = input("Syötä maakoodi: ")

palautus = hae_maakoodilla_lentoasemat(maaKoodi)
for i in palautus :
    print(i[0], i[1])