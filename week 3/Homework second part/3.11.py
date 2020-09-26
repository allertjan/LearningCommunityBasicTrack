import turtle

screen = turtle.Screen()

hour_turtle = turtle.Turtle()
hour_turtle.shape("turtle")
hour_turtle.left(90)
hour_turtle.penup()
hour_turtle.speed(1)

for hour in range(12):
    hour_turtle.forward(200)
    hour_turtle.pendown()
    hour_turtle.forward(25)
    hour_turtle.penup()
    hour_turtle.forward(25)
    hour_turtle.stamp()
    hour_turtle.backward(250)
    hour_turtle.right(30)

screen.exitonclick()
