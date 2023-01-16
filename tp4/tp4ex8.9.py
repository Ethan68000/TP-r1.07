dico = {}
dico['firstname'] = 'ethan'
dico['name'] = 'Coulon'
dico['promotion'] = '2022'
dico['group'] = '202'

binome = {}
binome['firstname'] = 'Florian'
binome['name'] = 'Mercklé'
binome['promotion'] = '2022'
binome['group'] = '202'

tuplets = {
    "name": dico['name'],
    "firstname": dico['firstname'],
    "promotion": dico['promotion'],
    "group": dico['group']
}

tuplets2 = {
    "name": binome['name'],
    "firstname": binome['firstname'],
    "promotion": binome['promotion'],
    "group": binome['group']
}

print("les etudiants formants le binôme sont:")
print("-L'étudiant {} {} du groupee {}".format(dico['name'], dico['firstname'], dico['group']))
print("-L'étudiant {} {} du group {}".format(binome['name'], binome['firstname'], binome['group']))