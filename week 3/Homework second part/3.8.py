import turtle
paper = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)

for polygon in range(18):
    alex.forward(30)
    alex.right(360/18)

paper.exitonclick()