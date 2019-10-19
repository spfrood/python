
import turtle
from random_colors import get_random_color

square = turtle.Turtle()
square.hideturtle()

for x in range (4):
  square.color(get_random_color())
  square.begin_fill()
  square.right(90)
  for y in range(4):
    square.forward(100)
    square.right(90)
  square.end_fill()

turtle.done()




