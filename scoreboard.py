from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(230, 270)
        self.score = 0
        self.write(f"Score:{self.score}", align="center", font=("Courier", 20, "normal"))
    def refresh(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
    def game_over(self):
        self.clone()
        self.goto(0,0)
        self.write("Game Over.", align="center", font=("Courier", 24, "normal"))
