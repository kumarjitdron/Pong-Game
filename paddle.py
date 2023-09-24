from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, xcr, ycr):
        super().__init__()
        self.goto(x=xcr, y=ycr)
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.shape("square")
        self.color("white")
        #self.setpos(360 , 0)
        #self.height(100)
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
