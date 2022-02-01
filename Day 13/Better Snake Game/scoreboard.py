import turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt", mode = "r") as file:
            for x in file.readlines():
                self.high_score = int(x)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updatescoreboard()
    
    def updatescoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.updatescoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.updatescoreboard()