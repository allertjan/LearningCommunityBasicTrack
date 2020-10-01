import turtle

coordinates = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

paper = turtle.Screen()
alex = turtle.Turtle()

for (angle, steps) in coordinates:
    alex.left(angle)
    alex.forward(steps)

paper.exitonclick()