x = float(input("Entre un nombre décimal:"))
if(x >= -10 and x <= -2) or (x > 0 and x <= 1) or (x >= 2 and x < 3):
   print(x,"appartient a I")

else:
    print(x, "n'apartient pas à I")


x = float(input("Entre un nombre décimal:"))
if (not x < -10 and x <= -2) or (not x <= 0 and x <= 1) or (not x < 2 and x < 3):
    print(x,"appartient a I")

else:
    print(x, "n'apartient pas à I")



