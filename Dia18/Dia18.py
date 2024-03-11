import turtle as TDraw
import random

#Obtener colores con la imagen
#import cologram
#rbgcolors=[]
#colors=colorgram.extract('C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia18/color.jpg', 30)
#print(colors)
#for color in colors:
#    r=color.rgb.r
#    g=color.rgb.g
#    b=color.rgb.b
#    newcolor=(r,g,b)
#    rbgcolors.append(newcolor)

rbgcolors=[(236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
TDraw.colormode(255)
turtle=TDraw.Turtle()

turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)
turtle.speed(0)
turtle.hideturtle()
for lines in range(10):
    for _ in range(10):
        turtle.dot(20,random.choice(rbgcolors))
        turtle.penup()
        turtle.forward(50)

    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)

    turtle.forward(500)
    turtle.setheading(0)

screen=TDraw.Screen()
screen.exitonclick()