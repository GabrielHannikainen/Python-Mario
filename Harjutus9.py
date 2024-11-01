#Harjutus 9
#Gabriel
#24.10.24


import random
"""
# Genereeri ja kuva arvud arvud 1-20
for i in range(20):
    print(i+1, end=" ")
# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# import random
# random.randint(min, max)
for i in range(1,21):
    print(random.randint(1, 99), end=" ")
print()
# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# Leia paaris ja paaritud arvud ning lisa oma loendisse
# Kuva paaris ja paritute arvude summad
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []
for i in loend:
    if i%2 == 0:
        paaris.append(i)
    else:
        paaritud.append(i)

print(f"paaris arvude summa on {sum(paaris)}")
print(f"paaritute arvude summa on {sum(paaritud)}")

print()
# Kuva arvud 1-42
# Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
for i in range(1,43):
    print(i, end=" ")
    if i%3 ==0 and i%5 == 0:
        print(i,"TIKTAK", end=" ")
    elif i%3==0:
        print(i,"TIK", end=" ")
    elif i%5==0:
        print(i,"TAK", end=" ")
    else:
        print(i, end=" ")




# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
#Harjutus 6
#Gabriel
#01.11.24

nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
unimed = []

for nimi in nimed:
    if nimi not in unimed:
        unimed.append(nimi)

print(unimed)


#Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.




ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
meeles = []



for opilane in ryhma_hinded:
    meeles.append(float(opilane.split(" ")[1]))

print(f"parim tulemus {max(meeles)}")
print(f"Halvim tulemus {min(meeles)}")
print(f"keskmine {round(sum(meeles)/len(meeles), 2)}")
"""
#Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:

#Näiteks:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#for i in range(11):
    #print(f"{i} x {i} = {i*i}")

#Kasuta tsükli puhul alakriipsu
#kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
#Näiteks:
#7 – 2=
#45 * 69=
#71 – 45=
"""
punktid = 0
tehted = ["+", "-", "*", "/"]
kysimuste_arv = 6

for i in range(6):
    j = random.randint(1, 10)
    k = random.randint(1, 10)
    tehe = random.choice(tehted)
    if tehe == "+":
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j+k:
            print("Õige vastus")
            punktid += 1
        else:
            print("Vale vastus")
            punktid -= 1
    elif tehe == "-":
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j-k:
            print("Õige vastus")
            punktid += 1
        else:
            print("Vale vastus")
            punktid -= 1
    if tehe == "*":
        print(f"{j} {tehe} {k} = ")
        vastus = int(input("Vastus: "))
        if vastus == j*k:
            print("Õige vastus")
            punktid += 1
        else:
            print("Vale vastus")
            punktid -= 1
    elif tehe == "/":
         print(f"{j} {tehe} {k} =")
         vastus = int(input("Vastus: "))
    if vastus == j/k:
            print("Õige vastus")
            punktid += 1
    else:
        print("Vale vastus")
        punktid -= 1
print(str(kysimuste_arv/punktid))*+"%"
if punktid/kysimuste_arv >= 0.5:
    print("A")
else:
    print(MA)

for i in range(1,6):
    print("*"*i)
print()
for i in range(1,6):
    print("*"* (6-i))
print()
for i in range(1,6):
    print(" "*(5-i) + "*"*i)
print()
for i in range(1,6):
    print(" "*(-1+i)+"*"*(6-i))

summa = 0
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
for i in even_nums:
    if i % 2 == 0:
        summa += i
    else:
        break

print(summa)

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

labisoit = []
hinnad = []
kolmsada = []
for car in ev_data:
    if car[1] != "range" or car[2] != "price":
        labisoit.append(int(car[1]))
        if int(car[1]) >=300:
            kolmsada.append(car[0])
        hinnad.append(int(car[2]))
        print(int(car[2])/int(car[1]))
    else:
        print("Ratio")
    
    for i in car:
        print(f"{i:30}", end=" ")
print()
print(f"Keskmine labisoit: {sum(labisoit)/len(labisoit)}")
print(f"Keskmine hind: {sum(hinnad)/len(hinnad)}")
print(kolmsada)

"""

    