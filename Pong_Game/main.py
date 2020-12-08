from turtle import Turtle, Screen

paddle = Turtle()
paddle.shape("square")
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.goto(350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.exitonclick()