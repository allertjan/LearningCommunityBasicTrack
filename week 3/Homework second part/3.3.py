import turtle
""" it will turn left by 3645 degrees. This will result in that the turtle does 10 turns of 360 degree and then another 
45 degree left. So 3645 is equal to 45 degree"""
paper = turtle.Screen()
rafael = turtle.Turtle()
alex = turtle.Turtle()

rafael.stamp()
rafael.left(3645)
rafael.forward(100)
rafael.color("red")
rafael.stamp()

alex.left(45)
alex.forward(100)
alex.stamp()

paper.exitonclick()