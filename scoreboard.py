from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.goto(0, 270)
        self.scoring()

    def scoring(self):
        self.clear()
        self.hideturtle()
        self.score += 1
        self.write(
            f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(
            "Game Over",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )
