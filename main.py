import turtle
from paddles import Paddle
from balls import Ball
import time
from score import Score
from border import Border

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Ping Pong")
screen.tracer(0)

paddle_right = Paddle(350)
paddle_left = Paddle(-360)

x = 300
for i in range(0, 50):
    border = Border(x)
    x -= 50


screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")


bounce = 'None'
re_bounce = 'None'
mag = True
left_score = 0
right_score = 0

while mag:
    pong_ball = Ball()
    flag = True
    left_score_display = Score("left", left_score)
    right_score_display = Score("right", right_score)
    while flag:
        time.sleep(0.04)

        if pong_ball.ycor() > 280:
            bounce = "Down"
        elif pong_ball.ycor() < -280:
            bounce = "Up"
        if pong_ball.distance(paddle_left.paddle) < 30:
            re_bounce = "east"
        elif pong_ball.distance(paddle_right.paddle) < 30:
            re_bounce = "west"

        pong_ball.ball_movement(bounce, re_bounce)

        if pong_ball.xcor() > 380:
            left_score += 1
            pong_ball.hideturtle()
            left_score_display.clear()

            break
        elif pong_ball.xcor() < -380:
            right_score += 1
            pong_ball.hideturtle()
            right_score_display.hideturtle()
            right_score_display.clear()
            break

        screen.update()

screen.exitonclick()
