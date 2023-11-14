from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='root',
    password='Ruutt!',
    autocommit=True
    )

app = Flask(__name__)
@app.route('/kenttä/<icao>')

def asema(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident = '" + icao + "'"

    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0 :
        for row in result:
            return {
                "ICAO": icao,
                "Name": row[0],
                "Municipality": row[1]
            }
    
def lentoasema(icao):
    return asema(icao)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)