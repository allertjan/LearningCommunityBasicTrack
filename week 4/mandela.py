import turtle


def make_turtle(color, size):
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    animal.speed(0)
    return animal


def make_window(color):
    window = turtle.Screen()
    window.bgcolor(color)
    return window


def make_figure(animal, size):
    for _ in range(8):
        animal.forward(size)
        animal.left(45)


wn = make_window("black")
redturtle = make_turtle("red", 5)
yellowturtle = make_turtle("yellow", 5)
blueturtle = make_turtle("blue", 5)
greenturtle = make_turtle("green", 5)


for _ in range(30):
    make_figure(redturtle, 60)
    redturtle.penup()
    redturtle.left(12)
    redturtle.forward(15)
    redturtle.pendown()

for _ in range(30):
    make_figure(yellowturtle, 30)
    yellowturtle.penup()
    yellowturtle.left(12)
    yellowturtle.forward(15)
    yellowturtle.pendown()

for _ in range(30):
    make_figure(blueturtle, 15)
    blueturtle.penup()
    blueturtle.left(12)
    blueturtle.forward(15)
    blueturtle.pendown()

for _ in range(32):
    make_figure(greenturtle, 7)
    greenturtle.penup()
    greenturtle.left(12)
    greenturtle.forward(15)
    greenturtle.pendown()

wn.exitonclick()


