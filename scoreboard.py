from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)
    
    def add_point(self):
        self.score += 1 
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER FINAL SCORE:{self.score}", align="center", font=FONT)