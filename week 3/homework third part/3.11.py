import turtle

paper = turtle.Screen()
alex = turtle.Turtle()

coordinates = [(270, 100), (45, 100), (90, 100), (45, 100), (90, 140), (145, 168), (215, 148), (212, 178)]

for (angle, steps) in coordinates:
    alex.right(angle)
    alex.forward(steps)

paper.exitonclick()