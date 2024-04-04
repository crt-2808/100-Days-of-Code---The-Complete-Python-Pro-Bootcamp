FONT = ("Courier", 24, "normal")
ALIGNMENT="center"
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.level +1}", align=ALIGNMENT, font=(FONT))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def addScore(self):
        self.level+=1
        self.clear()
        self.update_scoreboard()