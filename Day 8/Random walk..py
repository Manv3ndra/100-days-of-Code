import turtle, random

tim = turtle.Turtle()
turtle.colormode(255)

def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

directions = [0, 90, 180, 270]
tim.width(20)
tim.speed('fastest')

for i in range(1000):
    tim.color(random_colours())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()