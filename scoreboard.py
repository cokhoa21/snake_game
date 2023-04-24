from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.new_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.new_score} High Score : {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.new_score > self.high_score:
            self.high_score = self.new_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.new_score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.new_score += 1
        self.update_scoreboard()
