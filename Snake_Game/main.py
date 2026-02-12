from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_manager import GameManager
import time


# Screen Settings
screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
manager = GameManager(snake, food, scoreboard, screen)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(manager.reset, "y")
screen.onkey(manager.quit_game, "n")

game_playing = True

while game_playing:
    screen.update()

    if manager.is_game_on:
        time.sleep(0.1)
        snake.move_snake()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_score()
            snake.extend()

        # Detect collision with wall
        if abs(snake.head.xcor()) > 380 or abs(snake.head.ycor()) > 380:
            manager.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                manager.game_over()


screen.exitonclick()