#Harjutus4

#1.Aia pikkus
try: 
    failisuurus = int(input("Sisesta faili suurus (MB): "))
    downKiirus = int(input("Sisesta allalaadimise kiirus (MB/s): "))
    aeg = failisuurus / downKiirus
    print(f"Alla laadimiseks kulub {aeg:0.2f} sekundit.")
except:
    print("Sisestasid valesti")

"""
a = int(input("Sisesta külg 1 : "))
b = int(input("Sisesta külg 2 : "))
p = 2 * (a + b)
print(f"Aia kogupikkus on {p} meetrit.")
"""
#2. Raamatute allahindlus
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus
print(f"{kogus}sfsgs ada ada ada {summa:0.2f}£")