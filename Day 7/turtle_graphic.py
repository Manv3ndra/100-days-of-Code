from turtle import Turtle, Screen
import turtle,random

tim = Turtle()
tim.speed(0)
tim.pensize(5)
tim.shape('turtle')
screen = Screen()

'''
colour = ['red','blue','green','yellow','black']

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

def clickleft(x,y):
    tim.color(random.choice(colour))

def clickright(x,y):
    tim.stamp()

turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)

turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')

turtle.mainloop()
'''

def dragging(x,y):
    tim.ondrag(None)
    tim.setheading(tim.towards(x,y))
    tim.goto(x,y)
    tim.ondrag(dragging)

def clickright(x,y):
    tim.clear()

def clickleft(x,y):
    tim.penup()
    tim.goto(x,y)
    tim.pendown()

turtle.listen()

tim.ondrag(dragging)
turtle.onscreenclick(clickright, 3)
turtle.onscreenclick(clickleft, 1)

screen.mainloop()