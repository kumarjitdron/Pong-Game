from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
score = Score()

ball1 = Ball()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


is_game_on= True
while is_game_on:
    screen.update()
    time.sleep(ball1.move_speed)

    # detect collision with wall
    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce_y()

    # detect collision with right paddle
    if ball1.distance(paddle1) < 50  and ball1.xcor() > 320:
        ball1.bounce_x()

    # detect collision with left paddle
    if ball1.distance(paddle2) < 50 and ball1.xcor() < -320:
        ball1.bounce_x()

    # detect ball miss right paddle or not
    if ball1.xcor() > paddle1.xcor() + 20:
        ball1.home()
        ball1.bounce_x()
        ball1.move_speed = 0.1
        score.increase_lscore()

    # detect ball miss left paddle or not
    if ball1.xcor() < paddle2.xcor() - 20:
        ball1.home()
        ball1.bounce_x()
        ball1.move_speed = 0.1
        score.increase_rscore()


    ball1.move()


screen.exitonclick()
