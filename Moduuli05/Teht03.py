luku = int(input("Anna luku: "))
kohta = 1
virhe = False

#if luku % luku == 0 and luku % 1 == 0 :
for i in range(2, luku) :
    if luku % i == 0 :
        print(f"Luku {luku} ei ole alkuluku")
        virhe = True
        break
    
if virhe == False :
    print(f"Luku {luku} on alkuluku")
        

    
        