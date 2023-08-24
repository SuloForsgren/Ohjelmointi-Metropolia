ktunnus = "python"
salasana = "rules"
yritys = 0

while True:
    print("\n")
    if yritys == 5 :
        print("Pääsy evätty!")
        break

    user = str(input("Anna Käyttäjätunnus: "))
    password = str(input("Anna salasana: "))

    if user == ktunnus and password == salasana :
        print("Tervetuloa!")
        break

    yritys += 1