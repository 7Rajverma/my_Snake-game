from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt")as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()
        self.reset()

    def update_score(self):
        self.clear()         #score jaise increase ho waise hi purana score clear ho jaye
        self.write(f" Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w")as data:
                data.write(f"{self.high_score}")


        self.score = 0
        self.update_score()

    # def Gameover(self):
    #     self.goto(0,0)
    #     self.write(arg=" GAME OVER ", align=ALIGNMENT, font=FONT)

    def increase_score(self):  #ya hum score increse kr rahe hai but score ki value overlap kr rahi thi to hum ek aor
                               #method banaya (update score ka
        self.score+= 1
        self.update_score()     # fir ye wapas se score board ko le aaye with updated score