#Harjutus 16
#Gabriel
import datetime
import os
nimi = os.getlogin()

print(f"Tere {nimi}!")

print(f"Sa oled: {os.getcwd()}")

kokku = 3
x = datetime.datetime.now().strftime('%Y%m%d')
try:
    for i in range (kokku):
        kataloog = x+"_"+str(i+1)
        os.mkdir(kataloog)
        print(kataloog)
except:
    print("sul on juba need kataloogid")

valik = input("Lisa kataloog, mida kustutada : ")
try:
    os.rmdir(valik)
    print(valik+ " kustutatud")
except:
    print("Mingi jama kustutamisel")