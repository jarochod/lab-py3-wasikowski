# R169. Turtle - Gra Snake - implementacja klasy Snake

import turtle

class Snake:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    MOVE_DISTANCE = 20


    def __init__(self, startX, startY) -> None:
        self.startX = startX
        self.startY = startY
        self.segments = []
        self.refresh()

    def refresh(self):
        print("snake reset")

        self.segments = []
        self.addSegments(self.startX, self.startY)
        self.head = self.segments[0]
        self.direction = None

    def addSegments(self, x, y):
        t = turtle.Turtle("square")
        t.hideturtle()
        t.penup()
        t.goto(x,y)
        t.color("red")
        t.showturtle()
        self.segments.append(t)

    def keyUp(self):
        self.direction = Snake.UP

    def keyDown(self):
        self.direction = Snake.DOWN

    def keyLeft(self):
        self.direction = Snake.LEFT

    def keyRight(self):
        self.direction = Snake.RIGHT

    def move(self):
        headX = self.head.xcor()
        headY = self.head.ycor()

        if self.direction == Snake.UP:
            headY += Snake.MOVE_DISTANCE
        if self.direction == Snake.DOWN:
            headY -= Snake.MOVE_DISTANCE
        if self.direction == Snake.LEFT:
            headX -= Snake.MOVE_DISTANCE
        if self.direction == Snake.RIGHT:
            headX += Snake.MOVE_DISTANCE

        self.head.goto(headX, headY)