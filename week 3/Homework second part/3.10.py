import turtle
paper = turtle.Screen()
alex = turtle.Turtle()
alex.hideturtle()

for star in range(5):
    alex.forward(100)
    alex.right(144)

paper.exitonclick()