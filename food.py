from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)



