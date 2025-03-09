from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.x = 300
        self.y = 0
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle(shape="square")
        car.shapesize(stretch_len=3, stretch_wid=1)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        self.y = random.randint(-170, 250)
        car.goto(self.x, self.y)
        self.cars.append(car)

    def move_car(self,car):
        car.forward(self.move_speed)

    def upgrade_speed(self):
        self.move_speed += MOVE_INCREMENT
