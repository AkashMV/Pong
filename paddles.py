from turtle import Turtle


class Paddle:

    def __init__(self, x):
        self.paddle = Turtle(shape="square")
        self.paddle.setheading(90)
        self.paddle.turtlesize(stretch_wid=1, stretch_len=5)
        self.paddle.color("white")
        self.paddle.pu()
        self.paddle.goto(x=x, y=0)

    def up(self):
        if self.paddle.ycor() < 240:
            if self.paddle.xcor() > 0:
                self.paddle.goto(y=self.paddle.ycor()+20, x=350)
            else:
                self.paddle.goto(y=self.paddle.ycor() + 20, x=-360)

    def down(self):
        if self.paddle.ycor() > -240:
            if self.paddle.xcor() > 0:
                self.paddle.goto(y=self.paddle.ycor()-20, x=350)
            else:
                self.paddle.goto(y=self.paddle.ycor()-20, x=-360)
