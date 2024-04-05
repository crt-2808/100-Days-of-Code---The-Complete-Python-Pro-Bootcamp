from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        with open("C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia20/data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((0,270))
        self.updateScore()
    

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} HIGH SCORE:{self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            self.updateHighScore()
        self.score=0
        self.updateScore()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
    def addScore(self):
        self.score+=1
        self.updateScore()

    def updateHighScore(self):
        with open("C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia20/data.txt", mode="w") as data:
            actual_score=str(self.score)
            data.write(actual_score)