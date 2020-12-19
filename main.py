import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
car_manager = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.listen()
    car_manager.new_car()
    speed_level = 0
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.turtle_finished():
        player.reset()
        scoreboard.next_level()
        car_manager.speed_up()

screen.exitonclick()
