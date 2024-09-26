from turtle import Turtle
import random


class Food(Turtle):  #Turtle class se inherent hai to jo turtle class m hai wo iss m bhi ho ga
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.color("Green")
        self.speed("fastest")
        self.referesh()

    def referesh(self):
        x_coordinate = random.randint(-280,280)
        y_coordinate = random.randint(-280,280)             #ye food ko remdomly place krne k leye use hota hai
        self.goto(x_coordinate,y_coordinate)





