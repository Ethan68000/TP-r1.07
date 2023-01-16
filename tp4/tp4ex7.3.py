login1="Ethan"
login2="Antoine"
login3 = input("Quelle est le login du nouvelle étudiant : ")
binôme = (login1, login3)

print("Notre binome est composées de {} et {}".format(login1, login3))

del login3

print("Votre binome n'est plus composé de {}".format(login1))