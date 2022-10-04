from turtle import Turtle


class Snake:
    def __init__(self):
        super().__init__()
        self.all_turtles = []
        self.score = 0
        self.is_clear = True

    def make_snakes(self, num):
        a = 0
        if num == 3:
            for i in range(0, num):
                new_turtle = Turtle(shape="square")
                new_turtle.penup()
                new_turtle.color("white")
                new_turtle.goto(a, 0)
                self.all_turtles.append(new_turtle)
                a -= 20
        else:
            current_position_x = self.all_turtles[len(self.all_turtles)-1].xcor()
            current_position_y = self.all_turtles[len(self.all_turtles)-1].ycor()
            for i in range(0, num):
                new_turtle = Turtle(shape="square")
                new_turtle.penup()
                new_turtle.goto(current_position_x, current_position_y)
                self.all_turtles.append(new_turtle)
                new_turtle.color("white")
                a -= 20

    def extend(self):
        current_position = self.all_turtles[0].position()
        a = 4
        self.make_snakes(a)

    def move(self):
        for i in range(len(self.all_turtles) - 1, 0, -1):
            current_x = self.all_turtles[i - 1].xcor()
            current_y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].goto(current_x, current_y)
        self.all_turtles[0].forward(20)

    def up(self):
        if self.all_turtles[0].heading() != 270:
            self.all_turtles[0].setheading(90)

    def down(self):
        if self.all_turtles[0].heading() != 90:
            self.all_turtles[0].setheading(270)

    def left(self):
        if self.all_turtles[0].heading() != 360:
            self.all_turtles[0].setheading(180)

    def right(self):
        if self.all_turtles[0].heading() != 180:
            self.all_turtles[0].setheading(360)


