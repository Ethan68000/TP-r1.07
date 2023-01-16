jj = 0
mm = 0
année = 0

nMax = 31
n = int(input("Quelle est le jour que vous voulez"))
mMax = 3
m = int(input("Quelle est le mois que vous voulez"))
aMax = 3
a = int(input("Quelle est l'année que vous voulez"))
if n<0:
    print("Le jour n'est pas possible")
elif n>31:
    print("le jour doit être inférieur à 31")
elif m<0 or m>12:
    print("le mois n'est pas bon")
elif m==2 and n>28:
    print("cela n'est pas possible car février a seulement 28 jours")
elif m==4 or m==6 or m==9 or m==11 and n>30:
    print("Ces mois n'ont que 30 jours")
else:
    print("La date du {}{}{} est valide".format(n, m, a))