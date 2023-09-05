luku = int(input("Anna luku: "))
virhe = False

for i in range(2, luku) :
    if luku % i == 0 :
        print(f"Luku {luku} ei ole alkuluku")
        virhe = True
        break
    
if virhe == False :
    print(f"Luku {luku} on alkuluku")
        

    
        