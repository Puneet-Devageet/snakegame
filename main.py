from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    """adds 0.1sec delay to the screen """
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect Collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_one = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            # game_is_one = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()




screen.exitonclick()















