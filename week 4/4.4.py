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


def make_squares(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


wn = make_window("limegreen")
alex = make_turtle("hotpink", 5)

for _ in range(24):
    make_squares(alex, 200)
    alex.left(360 / 24)

wn.exitonclick()
