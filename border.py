from turtle import Turtle


class Border(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.seth(90)
        self.shapesize(stretch_wid=0.15, stretch_len=1)
        self.goto(0, x)
