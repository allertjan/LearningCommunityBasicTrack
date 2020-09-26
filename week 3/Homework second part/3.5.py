import turtle
paper = turtle.Screen()
rafael = turtle.Turtle()
rafael.color("red")
alex = turtle.Turtle()
alex.color("green")
tess = turtle.Turtle()
tess.color("blue")
pj = turtle.Turtle()

for triangle in range(3):
    rafael.forward(100)
    rafael.right(120)

for square in range(4):
    alex.forward(100)
    alex.left(90)

for hexagon in range(6):
    tess.forward(-100)
    tess.left(60)

for octagon in range(8):
    pj.forward(-100)
    pj.right(45)
