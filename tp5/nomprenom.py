prenom1=str(input("Entrez votre prénom"))
nom1=str(input("Entrez votre nom"))
prenom2=str(input("Entrez votre prénom"))
nom2=str(input("Entrez votre nom"))

str.capitalize(prenom1)
str.capitalize(prenom2)
str.upper(nom1)
str.upper(nom2)

if nom1 > nom2:
    print(prenom2 + nom2 +"\n" + prenom1 + nom1)
else:
    print(prenom1 + nom1 + "\n" + prenom2 + nom2)