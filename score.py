import turtle


class Score(turtle.Turtle):

    def __init__(self, paddle, score):
        super().__init__()
        self.ht()
        self.color("white")
        self.pu()
        self.paddle = paddle
        if paddle == "left":
            self.goto(x=-50, y=240)
            self.write(arg=f"{score}", align="center", font=("Courier", 40, "normal"))
        elif paddle == "right":
            self.goto(x=50, y=240)
            self.write(arg=f"{score}", align="center", font=("Courier", 40, "normal"))
