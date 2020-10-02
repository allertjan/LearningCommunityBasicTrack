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


alex = make_turtle("hotpink", 5)
wn = make_window("limegreen")
draw_polygon(alex, 8, 50)

wn.exitonclick()
