from turtle import Screen
import time
from snake import Snake

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()

screen.listen()
screen.onkey(snake.moveUp, "w")
screen.onkey(snake.moveDown, "s")
screen.onkey(snake.moveLeft, "a")
screen.onkey(snake.moveRight, "d")

game_in_on=True

while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()