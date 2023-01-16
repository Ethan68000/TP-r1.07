import random
n = random.randint(0,100)
vies = 10
appreciation = "?"
while vies > 0:
    var = input("Entrez un nombre")
    var = int(var)
    if var < n :
        appreciation = "trop bas"
        print(vies, appreciation)
    else :
        appreciation = "trop haut"
        print(vies, appreciation)
    if var == n:
        appreciation = "bravo !"
        print(vies, appreciation)
        break

    vies -= 1