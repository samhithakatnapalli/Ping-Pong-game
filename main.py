from turtle import Screen, Turtle
import time
from ball import Ball
from paddles import Paddle
from score import Score

screen = Screen()
screen.tracer(0)
screen.bgcolor("green")
screen.setup(width=800, height=600)

#paddles
right_paddle = Paddle(360)
left_paddle = Paddle(-360)

ball = Ball()
score = Score()

#key bindings
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

#the line in the middle
line = Turtle()
line.color("white")
line.pensize(2)
line.penup()
line.goto(0,400)
line.setheading(270)
for i in range(400):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

#ball movement and screen refresh
while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #detetcting collision with upper walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detecting collision with right and left paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    #detecting if ball goes past screen on right side (x-axis)
    if ball.xcor() > 390:
        ball.off_screen()
        score.l_score()

    # detecting if ball goes past screen on left side (x-axis)
    if ball.xcor() < -390:
        ball.off_screen()
        score.r_score()



screen.exitonclick()