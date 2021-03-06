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


def draw_polygon(animal, corners, size):
    for _ in range(corners):
        animal.forward(size)
        animal.left(360 / corners)


def draw_triangle(animal, size):
    draw_polygon(animal, 3, size)


wn = make_window("limegreen")
alex = make_turtle("hotpink", 5)
draw_triangle(alex, 90)

wn.exitonclick()
