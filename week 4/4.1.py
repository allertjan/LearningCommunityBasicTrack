import turtle


def make_squares(animal, steps, amount):
    animal.penup()
    animal.setposition(-350, 0)
    animal.pendown()
    for _ in range(amount):
        for _ in range(4):
            animal.forward(steps)
            animal.left(90)
        animal.penup()
        animal.forward(140)
        animal.pendown()


def make_turtle(color, size):
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal


def make_window(color):
    window = turtle.Screen()
    window.bgcolor(color)
    return window


wn = make_window("limegreen")
alex = make_turtle("hotpink", 5)
make_squares(alex, 90, 5)

wn.exitonclick()
