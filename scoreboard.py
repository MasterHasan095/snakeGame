from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)

        self.hideturtle()
        self.color("white")

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("arial", 24, "normal"))