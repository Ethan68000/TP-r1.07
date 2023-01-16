while True:
    n = int(input("Entrez un nombre: "))

    pair = ""
    positif = ""

    if n < 0:
        positif = "negatif"
    elif n > 0:
        positif= "positif"

    if n % 2 == 0:
        pair = "pair"
    else:
        pair = "impair"

    if n != 0:
        print("le nombre est ", positif, "et ", pair)
    else:
        print("le nombre est zéro et il est pair")