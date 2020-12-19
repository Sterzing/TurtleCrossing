from turtle import Turtle
import player
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        make_car = random.randint(1, 6)
        if make_car == 1:
            t = Turtle("square")
            t.penup()
            t.shapesize(1, 2)
            t.color(random.choice(COLORS))
            t.goto(300, random.randint(-240, 240))
            self.all_cars.append(t)

    def move(self):
        for car in self.all_cars:
            car.backward(self.current_speed)

    def speed_up(self):
        self.current_speed += MOVE_INCREMENT
