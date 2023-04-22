from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.new_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.new_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.new_score += 1
        self.clear()
        self.write(f"Score : {self.new_score}", align="center", font=("Arial", 24, "normal"))
