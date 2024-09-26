from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.create_snake()
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)     #  .01 second
    snake.move_snake()

    #detect the collision with food
    if snake.head.distance(food)<15:
        food.referesh()
        snake.extend()
        scoreboard.increase_score()
    # detect the collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect the collision with tail
    # if head collide with any segment of the tail then
    # execute game is over
    for segment in snake.segment[1:]:  # using slicing [1:] loop all the segment except 1 segment 
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()


