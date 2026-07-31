# R168. Turtle - Gra Snake - implementacja klasy Food

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        # shape = random.choice(["square", "circle", "triangle"])
        # color = random.choice(["blue", "silver", "orange"])
        shape = "square"
        color = "white"
        self.hideturtle()
        self.shape(shape)
        self.color(color)
        self.goto( random.randint(-200, 200), random.randint(-200, 200) )
        self.showturtle()


