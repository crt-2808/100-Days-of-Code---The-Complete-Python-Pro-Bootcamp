"""
pad=Turtle()
pad.shape("square")
pad.color("white")
pad.shapesize(stretch_wid=5, stretch_len=1)
pad.penup()
pad.goto(350,0)


def go_up():
    new_y=pad.ycor()+20
    pad.goto(pad.xcor(), new_y)

def go_down():
    new_y=pad.ycor()-20
    pad.goto(pad.xcor(), new_y)

"""
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(), new_y)
    
