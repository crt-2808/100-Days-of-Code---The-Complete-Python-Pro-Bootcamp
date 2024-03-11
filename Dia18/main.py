import turtle as t

turtle= t.Turtle()
turtle.shape("turtle")
turtle.color("green")

#Ejercicio 1
#for _ in range(4):
#    turtle.forward(10)
#    turtle.right()

#Ejercicio 2
#for _ in range(50):
#    turtle.forward(10)
#    turtle.penup()
#    turtle.forward(10)
#    turtle.pendown()

#Ejercicio 3
#import random
#shape_size=3
#color_turtle=["red", "green", "blue", "yellow", "cornflower blue", "maroon", "cyan"]
#while(shape_size != 11):
#    angle=360/shape_size
#    for _ in range (shape_size):
#        turtle.forward(100)
#        turtle.right(angle)
#    shape_size+=1
#    turtle.color(random.choice(color_turtle))

#Ejercicio 4
#import random
#turtle.speed(5)
#turtle.width(10)
#widthColor=10
#color_turtle=["red", "green", "blue", "yellow", "cornflower blue", "maroon", "cyan"]
#angle_turtle=[0, 90, 180, 270]
#for _ in range(250):
#    turtle.forward(25)
#    turtle.setheading(random.choice(angle_turtle))
#    turtle.color(random.choice(color_turtle))

#import random
#t.colormode(255)
#
#def random_color():
#    r=random.randint(0,255)
#    g=random.randint(0,255)
#    b=random.randint(0,255)
#    color_random=(r,g,b)
#    return color_random
#
#turtle.speed(5)
#turtle.width(10)
#widthColor=10
#angle_turtle=[0, 90, 180, 270]
#for _ in range(250):
#    turtle.forward(25)
#    turtle.setheading(random.choice(angle_turtle))
#    color=random_color()
#    turtle.color(color)
#


import random
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_random=(r,g,b)
    return color_random

turtle.speed(0)
turtle.width(1)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle.circle(120)
        turtle.setheading(turtle.heading() +10)
        turtle.color(random_color())

draw_spirograph(5)

screen=t.Screen()
screen.exitonclick()