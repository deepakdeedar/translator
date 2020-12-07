from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
timmy = Turtle()
timmy.speed("fastest")
for i in range(int(360/10)):
    timmy.circle(100)
    timmy._rotate(10)
    

screen = Screen()
screen.exitonclick()