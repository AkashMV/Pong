from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.pu()

    def ball_movement(self, bounce, re_bounce):
        temp_x = self.xcor()
        temp_y = self.ycor()

        if bounce == "None":
            temp_y += 10
        elif bounce == "Up":
            temp_y += 10
        elif bounce == "Down":
            temp_y -= 10

        if re_bounce == "None":
            temp_x += 10
        elif re_bounce == "west":
            temp_x -= 10
        elif re_bounce == "east":
            temp_x += 10

        self.goto(temp_x, temp_y)
