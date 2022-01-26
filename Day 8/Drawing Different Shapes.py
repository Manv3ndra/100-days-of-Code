import turtle, random

tim = turtle.Turtle()

tim.width(5)

colours = ['black','blue','midnight blue', 'steel blue', 'dark sea green', 'lime green', 'green yellow', 'yellow', 'orange', 'red', 'purple']

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for x in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(x)

screen = turtle.Screen()
screen.exitonclick()