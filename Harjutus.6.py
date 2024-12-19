#Harjutus 6
#Gabriel
#18.10.24

import turtle
import math

kordaja = 10
a = math.radians(53)
h = 4.4
x = abs(h / math.tan(a))
c = math.sqrt(x**2 + h**2)
print(x)
turtle.forward(x*kordaja)
turtle.left(90)
turtle.forward(h*kordaja)
turtle.left(180-(180-90-53))
turtle.forward(c*kordaja)



turtle.done()



import random

def korrutamine():
    # Loome juhuslikud arvud
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Korrutustehe
    print(f"Kui palju on {num1} * {num2}?")
    
    # Kasutaja sisend
    vastus = int(input("Sisesta oma vastus: "))
    
    # Kontrollime vastust
    if vastus == num1 * num2:
        print("Õige vastus!")
    else:
        print(f"Vale vastus. Õige vastus on {num1 * num2}.")
    
for i in range(10):
    korrutamine()


def vanused():
    vanused = [25, 30, 19, 40, 22, 18, 35]  # Näidispoole vanuseid

    suurim = max(vanused)
    vaikseim = min(vanused)
    kogusumma = sum(vanused)
    keskmine = kogusumma / len(vanused)
    
    print(f"Suurim vanus: {suurim}")
    print(f"Väikseim vanus: {vaikseim}")
    print(f"Kogusumma: {kogusumma}")
    print(f"Keskmine vanus: {keskmine}")

vanused()



def positiivsed_negatiivsed():
    positiivsed = []
    negatiivsed = []
    
    for i in range(5):
        arv = int(input(f"Palun sisesta {i+1}. arv: "))
        
        if arv > 0:
            positiivsed.append(arv)
        elif arv < 0:
            negatiivsed.append(arv)
        # Nulli puhul ei tee midagi
        
    print(f"Positiivsed arvud: {positiivsed}")
    print(f"Negatiivsed arvud: {negatiivsed}")

positiivsed_negatiivsed()


def eurokalkulaator():
    print("Vali valuutamuundus:")
    print("1. EUR -> EEK")
    print("2. EEK -> EUR")
    
    valik = int(input("Sisesta oma valik (1 või 2): "))
    
    if valik not in [1, 2]:
        print("Vale valik!")
        return
    
    summa = float(input("Sisesta summa: "))
    
    if valik == 1:
        # EUR -> EEK
        tulemus = summa * 15.6466  # 1 EUR = 15.6466 EEK
        print(f"{summa} EUR on {tulemus} EEK")
    elif valik == 2:
        # EEK -> EUR
        tulemus = summa / 15.6466
        print(f"{summa} EEK on {tulemus} EUR")
        
eurokalkulaator()


import random

def taringud():
    print("Täringumäng: Iga mängija viskab 2 täringut.")
    
    # Kasutaja viskab 2 täringut
    kasutaja_tulemus = random.randint(1, 6) + random.randint(1, 6)
    print(f"Kasvataja viskas: {kasutaja_tulemus}")
    
    # Arvuti viskab 2 täringut
    arvuti_tulemus = random.randint(1, 6) + random.randint(1, 6)
    print(f"Arvuti viskas: {arvuti_tulemus}")
    
    # Võitja määramine
    if kasutaja_tulemus > arvuti_tulemus:
        print("Sa võitsid!")
    elif kasutaja_tulemus < arvuti_tulemus:
        print("Arvuti võitis.")
    else:
        print("Viik!")

taringud()

