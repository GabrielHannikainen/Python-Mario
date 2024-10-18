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
turtle.left(180-37)
turtle.forward(c*kordaja)



turtle.done()