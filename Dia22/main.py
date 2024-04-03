from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "i")
screen.onkey(l_paddle.go_down, "k")

game_is_on=True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor()>350:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard() 
        
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard() 
        
screen.exitonclick()