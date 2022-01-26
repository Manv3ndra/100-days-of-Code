import turtle, random

tim = turtle.Turtle()
turtle.colormode(255)

def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

tim.speed('fastest')

def spirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_colours())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

spirograph(5)

screen = turtle.Screen()
screen.exitonclick()