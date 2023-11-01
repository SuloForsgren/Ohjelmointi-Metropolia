import requests

paikkakunta = input("Syötä paikkakunta: ")

API_KEY = "e0d77955ba7e9bde522cb6b1836d5157"
URL = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={paikkakunta}"

response = requests.get(URL)

if response.status_code == 200 :
    response = response.json()
    kelvin = response["main"]["temp"]
    tila = response["weather"][0]["description"]

    celsius= kelvin - 273.15

    print(f"{celsius:.2f} celsius, {tila}")

else:
    print(response)