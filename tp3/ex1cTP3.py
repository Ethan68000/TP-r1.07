a=0
b=0
c=0
for i in range (0, 10):
    x = int(input("entrer la valeur entre 0 et 20 : "))
    print(i+1)
    while x>20 or x<0:
        x = int(input("entrer la valeur entre 0 et 20 : "))
        print(1)
    if x<20 and x>0:
        if x<10:
            a=a+1
        elif x >=15:
            c=c+1
        else:
            b=b+1

print(f" Le nombre de valeurs inférieur strictement à 10 est {a}")
print(f" Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est {b}")
print(f" Le nombre de valeurs supérieur ou égale à 15 est {c}")


