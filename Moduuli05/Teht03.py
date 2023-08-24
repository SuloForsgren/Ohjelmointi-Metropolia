luku = int(input("Anna luku: "))
kohta = 1
for i in range(luku) :

    if kohta % luku == 0 and kohta != luku:
        break

    else :
        print(f"{luku} on alkuluku")
        

    kohta += 1