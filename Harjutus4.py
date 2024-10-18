#Harjutus4

#3 harjutus
"""
try: 
    failisuurus = int(input("Sisesta faili suurus (MB): "))
    downKiirus = int(input("Sisesta allalaadimise kiirus (MB/s): "))
    aeg = failisuurus / downKiirus
    print(f"Alla laadimiseks kulub {aeg:0.2f} sekundit.")
except:
    print("Sisestasid valesti")
"""
"""
#1.Aia pikkus
a = int(input("Sisesta külg 1 : "))
b = int(input("Sisesta külg 2 : "))
p = 2 * (a + b)
print(f"Aia kogupikkus on {p} meetrit.")
"""
#2. Raamatute allahindlus
"""
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus
print(f"{kogus}sfsgs ada ada ada {summa:0.2f}£")
"""
#4. Kingituste pakkimine
"""
try: 
    kingitused = int(input("Sisesta kingituste arv: "))
    maht = 5
    pakid = kingitused // maht
    ylejaak = kingitused % maht
    print(f"Saad {pakid} pakki ja {ylejaak} kingitust jääb üle.")
except:
    print("Sisestasid valesti") 
"""

 #5 Ringipindala
import turtle
try: 
    r = int(input("Sisesta ringi raadius: "))
    pi = 3.14
    s = pi*r**2
    p = 2*pi*r
    print(f"Ringi pindala on {s:0.2f} ja ümbermõõt on {p:0.2f}")
    turtle.circle(r, 360)
except: 
     print("Sisestasid valesti")
