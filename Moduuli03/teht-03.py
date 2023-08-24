suku = input("Syötä sukupuolesi: ")
hemo = int(input("Syötä hemoglobiini arvosi: "))
suku = suku.lower()

if suku == "nainen" :
    if hemo < 117 :
        print("Alhainen")
    elif hemo >= 117 and hemo <= 175 :
        print("Normaali")
    else :
        print("Korkea")

elif suku == "mies" :
    if hemo < 134 :
        print("Alhainen")
    elif hemo >= 134 and hemo <= 195 :
        print("Normaali")
    else :
        print("Korkea")
