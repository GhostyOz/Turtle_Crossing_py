from turtle import Turtle
class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
    def up(self):
        self.setheading(90)
        self.forward(10)
    def down(self):
        self.setheading(90)
        self.backward(10)
    def move_left(self):
        self.setheading(180)
        self.forward(10)
    def move_right(self):
        self.setheading(0)
        self.forward(10)