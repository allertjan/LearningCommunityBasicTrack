import turtle
paper = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for turn_degree in turns:
    alex.left(turn_degree)
    alex.forward(100)
print("Final heading is", sum(turns) % 360)


paper.exitonclick()



