#Harjutus 5
#Gabriel
#18.10.24


#4.Mündiviskamine
#1 Kiri
#0 Kull
import turtle
import random
suv = random.randint(0, 1)
kasutaja_valik = input("Kull või kiri:")
if suv == 1 and kasutaja_valik == "Kull":
    varv = "green"
else:
    varv = "red"
print(suv)
turtle.color(varv)
turtle.circle(50, 360)
turtle.done()


"""
import random
#3. Matemaatika test (randint)
a, b = random.randint(1, 10), random.randint(1, 10)
vastus = int(input(f"{a} * {b} = "))
if vastus == a*b:
    print("Õige vastus")
else: 
    print("Vale vastus")



#2 Ilmaennustuse rakendus (and)
c = 15
if c < 0:
    print("Külm")
elif c > 0 and c < 15:
    print("Kevad-Sügis")
else:
    print("Suvi")


#1 Vanusepiiranguga üritus 
vanus = 18
if vanus >= 18:
    print("Molli saad")
else:
   print("Ei saa sisse")
"""