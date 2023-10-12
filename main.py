import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

# car_manager.random_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # car_manager.moving_car()
