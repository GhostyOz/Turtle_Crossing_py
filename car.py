from turtle import Turtle
import random
COLORS = ['blue','red','green','yellow','magenta','cyan','orange','pink']

class CarManager:
    def __init__(self):
        self.cars = []
    def create_car(self,num_cars):
        for i in range(num_cars):
            num = random.randint(1,6)
            if num ==1:
                car = Turtle('square')
                car.shapesize(1,2)
                car.penup()
                car.speed('slowest')
                car.goto(+280, random.randint(-230, 230))
                car.color(random.choice(COLORS))
                car.setheading(180)
                self.cars.append(car)
        return self.cars


    def move_cars(self, cars,increment_value):
        for car in cars:
            if car.xcor() > -270:
                car.forward(increment_value)
            else:
                car.hideturtle()

