#Kujundid 7,10,13
#Gabriel Hännikäinen
#IT24

import turtle
turtle.speed("fastest")

#Kujund 7

for i in range(8):
    turtle.forward(10)
    turtle.right(45)

turtle.left(90)
for i in range(8):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)


turtle.penup()
turtle.goto(150,150)
turtle.pendown()

#Kujund 10

for i in range(2):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(65)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(100)

turtle.right(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(65)
turtle.left(90)

for i in range(2): 
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(100)

turtle.left(90)
turtle.forward(130)
turtle.left(180)
turtle.forward(65)
turtle.right(90)
turtle.forward(40)


turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

#Kujund 13
for i in range(5):
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(50)
    turtle.right(72)

turtle.done()
