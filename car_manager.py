from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__(self)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        
        
        
    def random_car(self):
        self.goto(x=300, y=random.randint(-280, 280))
        self.color(COLORS[random.randint(0, 5)])

    
    def moving_car(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
        
