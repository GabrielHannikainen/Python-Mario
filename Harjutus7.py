#22.10.24 Gabriel
#Ülesanded 7 loendid

#12 Kuud
import datetime
kuud = [["jaanuar",-18,-17,21,21,30,10,-19,-17,-2,5,-17,-2,-4,9,3,-13,-12,21,27,11,3,-11,-7,24,10,-10,14,29,7,17,-13],
["veebruar",0,2,-19,10,24,0,-8,-17,-10,22,17,-20,13,-1,-7,-18,4,17,-3,-3,7,-4,14,22,-10,25,7,21],
["märts,18",13,29,-1,5,-7,-11,8,26,4,-12,28,-17,16,5,13,30,-16,-15,3,26,-3,-15,10,-5,1,10,-1,5,18,-19],
["aprill",-8,9,26,-10,8,24,-5,20,14,23,1,-13,-18,26,12,22,-15,27,0,4,16,4,13,3,-20,6,-7,-19,-13,-1],
["mai",21,-18,26,-18,19,-10,-19,-8,-17,6,-17,-7,30,-4,30,-3,-1,27,-7,-14,-3,-6,-11,-12,-7,1,-10,12,-5,0,7],
["juuni",27,6,-15,22,25,-13,-18,3,21,20,26,-4,28,8,24,-12,6,-8,8,-14,26,-1,15,8,30,21,-13,-11,12,19],
["juuli",23,28,12,3,10,24,18,-18,29,19,21,-3,12,0,29,26,-20,6,-10,11,5,30,-12,7,-6,-13,10,-16,28,-14,-8],
["august",11,20,-19,-15,-11,0,-19,-9,5,17,26,-16,-14,26,-18,21,15,22,2,19,-8,3,-14,23,3,3,20,-12,-11,-6,-17],
["september",3,-13,-20,7,5,17,2,-4,-11,14,21,-16,4,2,10,11,-4,28,30,13,11,20,-8,13,-1,-7,27,0,-20,-3],
["oktoober",30,11,-14,8,2,3,21,5,9,11,-4,15,-1,18,30,-8,24,-2,11,4,-18,15,13,12,3,14,-5,13,1,-5,-15],
["november",30,-4,24,-13,-7,-17,-12,8,-15,-13,29,-12,9,21,0,-2,17,-13,-13,-9,-9,-18,23,24,-16,-12,2,11,22,15],
["detsember",-10,4,7,-6,-3,-1,-7,13,8,11,3,17,0,-3,22,-2,4,30,7,20,19,12,11,19,13,-8,-5,-12,2,19,2]]
print(kuud[9])
#Tänane kuu number
x = datetime.datetime.now()
tana = int(x.strftime("%m")) - 1 #-1 , et loendiga ühildada
#Tänase kuu andmed
print(kuud[tana][0])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine = []
for i in range(len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end = " ")
print(f"max temp: {max(ajutine)}")
print(f"min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")

print(f"-20 esineb {ajutine.count(-20)} korda")

ajutine.pop(5)
print(ajutine)


"""
muusika = ['ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"','Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"',]
for i in range(len(muusika)):
    print(str(i+1) + ". " + muusika[i])

try:
    valik = int(input("Vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    ("Midagi läks katki.Teavita adminni")
"""
