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


def make_picture(animal, steps,):
    animal.left(90)
    for _ in range(120):
        animal.forward(steps)
        animal.right(89)
        steps += 2
    alex.forward(steps + 2)
    alex.right(90)


wn = make_window("limegreen")
alex = make_turtle("blue", 1)
make_picture(alex, 3)

wn.exitonclick()
