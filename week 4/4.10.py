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


def make_star(animal):
    for _ in range(5):
        animal.forward(100)
        animal.right(144)


wn = make_window("limegreen")
alex = make_turtle("hotpink", 5)

for _ in range(5):
    make_star(alex)
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()


wn.exitonclick()