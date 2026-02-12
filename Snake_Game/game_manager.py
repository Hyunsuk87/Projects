from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

class GameManager:
    def __init__(self, snake, food, scoreboard, screen):
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.screen = screen
        self.is_game_on = True

    def game_over(self):
        self.is_game_on = False
        self.scoreboard.game_over()
        self.scoreboard.ask_replay()

    def reset(self):
        if not self.is_game_on:
            self.snake.reset_snake()
            self.food.refresh()
            self.scoreboard.reset_score()
            self.scoreboard.score = 0
            self.scoreboard.update_score()
            self.is_game_on = True

    def quit_game(self):
        self.screen.bye()