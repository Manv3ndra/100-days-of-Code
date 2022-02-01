import turtle as t
import random
import time
from player import Player
from cars import Car
from score import Score

screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.title("Crossy Road")
screen.tracer(0)

player = Player()
cars = Car()
scoreboard = Score()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()