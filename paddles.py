from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x_pos,0)

    def up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(),self.ycor()+60)
    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(),self.ycor()-60)