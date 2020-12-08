from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.score = 0
        self.update()
    
    def update(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()