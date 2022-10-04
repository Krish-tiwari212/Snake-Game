from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
is_clear = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark slate gray")
screen.title("Snake game")
screen.tracer(0)
new = Snake()
new.make_snakes(3)
screen.listen()
screen.onkey(new.up, "w")
screen.onkey(new.down, "s")
screen.onkey(new.left, "a")
screen.onkey(new.right, "d")

score = Scoreboard()
food = Food()

game_is_on = True
food.make_food()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    new.move()
    score.show_Score()
    score.border()
    if new.all_turtles[0].distance(food.position()) < 14:
        food.refresh()
        score.increase_score()
        new.extend()

    if new.all_turtles[0].xcor() > 270 or new.all_turtles[0].xcor() < -270 or new.all_turtles[0].ycor() > 170 or \
            new.all_turtles[0].ycor() < -270:
        score.border()
        game_is_on = False
        score.game_over()

    for segments in new.all_turtles[1:]:
        if new.all_turtles[0].distance(segments) < 10:
            score.border()
            game_is_on = False
            score.game_over()


screen.exitonclick()
