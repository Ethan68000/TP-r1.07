Moyenne = 0
notes = True
S2 = []
S3 = []
S4 = []
for i in range(5):
    S1 = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant"))
    S2 = S1.split(" ")
    S3.append(int(S2[0]))
    S4.append(int(S2[1]))

for i in range(4):
    Moyenne += S3[i] + S4[i]

for i in range(4):
    if S3[i] < 8:
        print("La note est inférieur à 8, vous n'êtes pas admis")
        notes = False

if notes == True:
    if Moyenne >=10:
        print("Vous êtes Admis")
    else:
        print("Vous n'êtes pas admis")