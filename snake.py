from turtle import Turtle ,Screen

POSITION = [(0, 0), (-20, 0), (-40,0)]
MOVE = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

   def __init__(self):
       self.segment = []
       self.create_snake()
       self.head = self.segment[0]

   def create_snake(self):
       for snake_seg in POSITION:
           self.add_snake(snake_seg)

   def reset(self):
       for seg in self.segment:
           seg.goto(1000,1000)
       self.segment.clear()
       self.create_snake()
       self.head = self.segment[0]


   def add_snake(self, snake_seg):
       tim = Turtle()
       tim.color("white")
       tim.shape("square")
       tim.penup()
       tim.goto(snake_seg)
       self.segment.append(tim)

   def extend(self):
       self.add_snake(self.segment[-1].position())



   def move_snake(self):
       for snake_seg in range(len(self.segment) - 1, 0, -1):
           new_x_snake = self.segment[snake_seg - 1].xcor()
           new_y_snake = self.segment[snake_seg - 1].ycor()
           self.segment[snake_seg].goto(new_x_snake, new_y_snake)
       self.head.forward(MOVE)

   def up(self):
       if self.head.heading()!=DOWN:
        self.head.setheading(UP)
   def down(self):
       if self.head.heading() != UP:
        self.head.setheading(DOWN)

   def right(self):
       if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

   def left(self):
       if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)