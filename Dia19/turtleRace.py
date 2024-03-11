from turtle import Turtle, Screen
import random


color=["red", "green", "orange", "yellow", "blue", "purple"]
y_pos=[-70, -40, -10, 20, 50, 80]
all_turtles=[]
is_race_on=False


screen=Screen()
screen.setup(width=500,height=400)
userBet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a color: ")
print(userBet)


for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
if userBet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==userBet:
                print(f"You've won. The winner is {winning_turtle} turtle.")
                
            else:
                print(f"You've lost. The winner is {winning_turtle} turtle.")

        randomdistance=random.randint(0,10)
        turtle.forward(randomdistance)

screen.exitonclick()