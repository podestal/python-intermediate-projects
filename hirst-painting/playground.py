from turtle import Screen
import turtle as t
import random

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

# n_lines = 3
# distance = 100

# while n_lines < 8:

#     angle = int(360 / n_lines)
#     for _ in range(n_lines):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#     n_lines += 1
#     distance += 20

############### Random Walk #############

# my_turtle = t.Turtle()
# t.colormode(255)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r, g, b)

# directions = [0, 90, 180, 270]
# my_turtle.pensize(15)
# my_turtle.speed('fastest')

# for _ in range(400):
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(directions))

############### Spirograph #############

jack = t.Turtle()
t.colormode(255)

counter = 10
jack.speed('fastest')

while counter <= 720:
    jack.color(random_color())
    jack.circle(100)
    jack.forward(10)
    jack.right(10)
    counter += 10


screen = Screen()
screen.exitonclick()