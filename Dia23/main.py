import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The turtle Crossing Game")
screen.listen()


player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()

game_is_on = True
screen.onkey(player.go_up, "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Choque con coches
    for car in car_manager.all_cars:
        if car.distance(player)<25:
            game_is_on=False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_start()
        car_manager.level_up()
        scoreboard.addScore()


screen.exitonclick()