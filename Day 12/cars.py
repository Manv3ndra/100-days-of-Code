import turtle
import random

COLORS = ['red', 'blue', 'yellow', 'black', 'green', 'orange', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = turtle.Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT