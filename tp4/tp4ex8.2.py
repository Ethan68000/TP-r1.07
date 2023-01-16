dico = {}
dico['firstname'] = 'ethan'
dico['name'] = 'Coulon'
dico['promotion'] = '2022'
dico['group'] = '202'

tuplets = {
    "name": dico['name'],
    "firstname": dico['firstname'],
    "promotion": dico['promotion'],
    "group": dico['group']
}
print("les clés du dictionnaires sont:")
for key, value in tuplets.items():
    print(key)
print("les valeurs du dictionnaires sont:")
for key, value in tuplets.items():
    print(value)
print("les tuplets du dictionnaires sont:")
for key, value in tuplets.items():
    print(key + ":" + value)