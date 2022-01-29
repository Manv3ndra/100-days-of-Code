from ctypes import alignment
import turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)