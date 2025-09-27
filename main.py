from turtle import Screen
from character import Character
from scoreboard import Scoreboard
from car import CarManager
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
ozzy = Character()
Cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(ozzy.up, "Up")
screen.onkey(ozzy.down, "Down")
screen.onkey(ozzy.move_left, "Left")
screen.onkey(ozzy.move_right, "Right")

game_on = True
game_valid = True
increment_value = 5
level = 1
while game_on:
    if level ==5:
        game_on = False
        pass
    increment_value = 5
    game_valid = True
    while game_valid:
        time.sleep(0.1)
        screen.update()
        cars = Cars.create_car(1)
        Cars.move_cars(cars,increment_value)
        for car in cars:
            if ozzy.distance(car) < 10:
                scoreboard.game_over()
                game_on = False
                break
        # If the level is passed
        if ozzy.ycor() >280:
            scoreboard.refresh()
            ozzy.goto(0, -280)
            game_valid = False

screen.exitonclick()
