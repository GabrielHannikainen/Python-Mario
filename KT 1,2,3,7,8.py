#1 Korrutamise ülesanne Gabriel
import random

nr1 = random.randint(1, 15)
nr2 = random.randint (1, 15)

print(f"Kui palju on {nr1} * {nr2}?")

vastus = int(input("vastus siia: "))

if vastus == nr1 * nr2:
    print("õige vastus!")
else:
    print(f"vale, õige vastus {nr1} * {nr2}")


#2 Vanused Gabriel

# vanused = [37, 24, 16, 19, 47, 11, 55]

# suurim = max(vanused)
# vaikseim = min(vanused)
# kogusumma = sum(vanused)
# keskmine = kogusumma/ len(vanused)

# print(f"vanim: {suurim}")
# print(f"noorim: {vaikseim}")
# print(f"kogu vanused: {kogusumma}")
# print(f"keskmine: {keskmine}")

# #3 Positiivsed ja Negatiivsed Gabriel

# positiivsed = []
# negatiivsed = []

# for i in range(5):
#     arv = int(input(f"Sisesta {i+1}. arv: "))
#     if arv > 0:
#         positiivsed.append(arv)
#     elif arv < 0:
#         negatiivsed.append(arv)

# print(f"Positiivsed arvud: {positiivsed}")
# print(f"Negatiivsed arvud: {negatiivsed}")