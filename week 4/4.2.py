import turtle


def make_turtle(color, size):
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal


def make_window(color):
    window = turtle.Screen()
    window.bgcolor(color)
    return window


def draw_square(animal, steps):
    for _ in range(4):
        animal.forward(steps)
        animal.left(90)


alex = make_turtle("hotpink", 5)
wn = make_window("limegreen")
steps = 90
for _ in range(10):
    draw_square(alex, steps)
    alex.right(135)
    alex.penup()
    alex.forward(20)
    alex.pendown()
    alex.left(135)
    steps += 30

wn.exitonclick()
