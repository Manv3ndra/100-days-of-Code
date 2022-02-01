import turtle

FONT = ('Courier', 20, 'normal')

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)