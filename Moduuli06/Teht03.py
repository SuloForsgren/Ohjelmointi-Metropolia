def bensiini(gallona) :
    lasku = gallona * 3.785
    return lasku

while True :
    gallonat = int(input("Anna gallonat: "))
    if gallonat < 0 :
        break
    palautus = bensiini(gallonat)
    print(f"{gallonat} gallonaa on {palautus} litraa")