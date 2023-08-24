sentit = 2.54

while True: 
    tuuma = int(input("Anna kokonaisluku: "))
    muunnos = sentit * tuuma
    
    if tuuma < 0 :
        break
    print(muunnos)