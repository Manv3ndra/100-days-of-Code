import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
color_list = ['red','blue','black','pink','yellow','purple', 'violet','lime','light sky blue','silver']

tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()