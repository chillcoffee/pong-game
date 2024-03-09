from turtle import Screen
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.forward(500)

screen.exitonclick()
