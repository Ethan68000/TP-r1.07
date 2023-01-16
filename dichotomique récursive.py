def recherche_dichotomie(tab, val):
    gauche = 0
    droite = len(ab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tab[milieu] ==val:
            return milieu
        elif tab[milieu] > val:
            droite = milieu - 1
        else:
            gauche = milieu + 1

