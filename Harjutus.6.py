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



7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
	kĆ¼sitakse valuuta kogust ja tehakse arvutused - 2p
	kood kommenteeritud - 1p
	
8. TĆ¤ringud
	kuvatakse korrektne arusaadav kĆ¼simus ja hiljem vastus - 1p
	kasutaja vĆµistleb kahe tĆ¤ringuga arvuti vastu - 1p
	kasutaja teeb pakkumise ning suurima tĆ¤ringupunktisumma vĆµitja saab laual oleva raha endale - 2p
	kood kommenteeritud - 1p
