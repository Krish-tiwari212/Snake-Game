from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def show_Score(self):
        self.clear()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(-100, 220)
        self.write(f"Score: {self.score}", font=("normal", 30, "bold"))
        self.hideturtle()

    def border(self):
        self.speed("fastest")
        self.penup()
        self.goto(0, 180)
        self.pendown()
        self.setheading(0)
        self.pendown()
        self.color("white")
        self.forward(280)
        self.right(90)
        self.forward(460)
        self.right(90)
        self.forward(560)
        self.right(90)
        self.forward(460)
        self.right(90)
        self.forward(280)

    def game_over(self):
        self.penup()
        self.goto(-100, 0)
        self.pendown()
        self.color("red")
        self.write(f"Game Over!", font=("normal", 30, "bold"))

    def increase_score(self):
        self.score += 1
