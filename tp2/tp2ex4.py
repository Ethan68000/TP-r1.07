Base = int(input("Entrez le nombre de personne(s) conviées à la fondue:"))
print("Pour faire une fondue fribourgeoise pour" , Base , "personnes, il vous faut :")
quantitédebase = 4
quantitédebasefromage = 800
quantitédebaseeau = 2
quantitédebaseail = 2
quantitédebasepain = 400
grammefromage = quantitédebasefromage * Base / quantitédebase
grammeeau = quantitédebaseeau * Base / quantitédebase
grammeail = quantitédebaseail * Base / quantitédebase
grammepain = quantitédebasepain * Base / quantitédebase
print("{} gr de fromage".format(grammefromage))
print("{} dl d'eau".format(grammeeau))
print("{} gousse(s) d'ail".format(grammeail))
print("{} gr de pain".format(grammepain))

