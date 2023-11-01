import requests

URL = "https://api.chucknorris.io/jokes/random"

response = requests.get(URL)
response = response.json()

print(response["value"])