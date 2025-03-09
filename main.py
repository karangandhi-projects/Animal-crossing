from turtle import Screen
import time

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

LEVEL_POSITION = (-250,270)

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player1 = Player()
level = Scoreboard(LEVEL_POSITION)
car_manager = CarManager()

wait_time = 0

screen.listen()
screen.onkey(player1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if wait_time == 0:
        car_manager.create_car()
        wait_time = 5

    for car in car_manager.cars:
        car_manager.move_car(car)
        if car.distance(player1) < 20:
            level.game_over()
            game_is_on = False

        if car.xcor() >= 300:
            car_manager.cars.remove(car)

    if player1.ycor() >= player.FINISH_LINE_Y:
        level.update_score()
        car_manager.upgrade_speed()
        player1.reset_player()

    wait_time-=1




screen.exitonclick()