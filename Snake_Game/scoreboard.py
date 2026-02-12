from turtle import Turtle


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 380)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 13, "normal"))

    def reset_score(self):
        self.clear()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 380)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 30)
        self.write("Game Over", False, align="center", font=("Arial", 30, "normal"))

    def ask_replay(self):
        self.goto(0, -50)
        self.color("sky blue")
        self.write("Do you wanna play one more round? (y: Yes / n: No)", False, align="center", font=("Arial", 15, "normal"))

