import random
from turtle import Turtle, Screen

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

drawer = Turtle()
drawer.pensize(3)

drawer.forward(100)

screen = Screen()
screen.exitonclick()
