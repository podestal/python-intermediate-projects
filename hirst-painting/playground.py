from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.color('blue')

############## Drawing a square ##########

# for _ in range(4):
#     my_turtle.forward(200)
#     my_turtle.right(90)

############## Dash line ###################

# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

############## Drawing different shapes ###########

n_lines = 3
distance = 100

while n_lines < 8:

    angle = int(360 / n_lines)
    for _ in range(n_lines):
        my_turtle.forward(100)
        my_turtle.right(angle)
    n_lines += 1
    distance += 20











screen = Screen()
screen.exitonclick()