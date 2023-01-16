def tri_cocktail(tab):
    echange = True
    debut = 0
    fin = len(tab) - 2
    while echange:
        echange = False
        for i in range(0, len(tab) - 1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                echange = True
        for i in range(len(tab) - 2, -1, -1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                echange = True
    print(tab)

a = [5, 2, 4, 8, 1, 3]
print(a)
tri_cocktail(a)