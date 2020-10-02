import turtle

window = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)


def make_figure(animal, steps):
    for _ in range(4):
        animal.forward(steps)
        animal.right(90)


def make_triangle(animal, steps):
    for _ in range(3):
        animal.forward(steps)
        animal.right(120)


for _ in range(60):
    make_figure(alex, 90)
    alex.right(6)
    alex.forward(15)

alex.left(90)
alex.penup()
alex.forward(190)
alex.right(90)
alex.color("red")
alex.pendown()

for _ in range(60):
    make_triangle(alex, 90)
    alex.right(6)
    alex.forward(15)




window.exitonclick()
