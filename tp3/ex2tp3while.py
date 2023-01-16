from time import sleep

n = int(input("entrer une valeur positive: "))

while(n+1):
    sleep(0.2)
    print(n)
    n=n-1