import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.forward(100)

leonardo.stamp()
leonardo.penup()
leonardo.forward(100)
leonardo.pendown()
leonardo.pensize(1)
leonardo.forward(100)

for element in [0, 1, 2, 3, 4, 5]:
    leonardo.forward(50)
    leonardo.left(60)
paper.exitonclick()
