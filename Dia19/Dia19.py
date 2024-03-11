from turtle import Turtle, Screen


turtle=Turtle()

def move_Forward():
    turtle.forward(50)

def move_Backward():
    turtle.backward(50)

def turnLeft():
    newHeading=turtle.heading()+10
    turtle.setheading(newHeading)

def turnRight():
    newHeading=turtle.heading()-10
    turtle.setheading(newHeading)

def penUp():
    turtle.penup()

def penDown():
    turtle.pendown()


def cleanScreen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen=Screen()
screen.listen()
screen.onkey(key="w", fun=move_Forward)
screen.onkey(key="s", fun=move_Backward)
screen.onkey(key="a", fun=turnLeft)
screen.onkey(key="d", fun=turnRight)
screen.onkey(key="q", fun=penUp)
screen.onkey(key="e", fun=penDown)
screen.onkey(key="c", fun=cleanScreen)


screen.exitonclick()