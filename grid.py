# [W02] DRILL#4 'grid.py' - 2019180048 윤여건
import turtle

turtle.speed(10)
width = 500
height = 500
gap = 100
pos = 0

while (pos <= height):
    turtle.penup()
    turtle.goto(0, pos)
    turtle.pendown()
    turtle.forward(width)
    pos += gap

pos = 0
turtle.left(90)

while (pos <= width):
    turtle.penup()
    turtle.goto(pos, 0)
    turtle.pendown()
    turtle.forward(height)
    pos += gap

turtle.exitonclick()
