from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()
        self.goto(position)
        self.points = 0
        self.update_score()

    def update_score(self):
        self.points += 1
        self.clear()
        self.write(arg=f"Level: {self.points}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", move=False, align=ALIGNMENT, font=FONT)