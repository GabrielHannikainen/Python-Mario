#1 Korrutamise ülesanne Gabriel
"""
import random

def korrutus_tehe():
   nr1 = random.randint(1, 15)
   nr2 = random.randint (1, 15)

   print(f"Kui palju on {nr1} * {nr2}?")

   vastus = int(input("vastus siia: "))

   if vastus == nr1 * nr2:
        print("õige vastus!")
    else:
        print(f"vale, õige vastus {nr1} * {nr2}")

for i in range(10):
    korrutus_tehe()
"""
#2 Vanused Gabriel
"""
def vanused():
    vanused = [37, 24, 16, 19, 47, 11, 55]

    suurim = max(vanused)
    vaikseim = min(vanused)
    kogusumma = sum(vanused)
    keskmine = kogusumma/ len(vanused)

    print(f"vanim: {suurim}")
    print(f"noorim: {vaikseim}")
    print(f"kogu vanused: {kogusumma}")
    print(f"keskmine: {keskmine}")
"""
#3 Positiivsed ja Negatiivsed Gabriel
"""
positiivsed = []
negatiivsed = []
for i in range(5):
    arv = int(input(f"sisesta {i+1}arv : "))
    if arv > 0:
        positiivsed.append[]
    elif arv < 0:
        negatiivsed.append[]
    print(f"positiivsed arvud:{positiivsed}")
    print(f"negatiivsed arvud: {negatiivsed}")
"""
print("hello world")