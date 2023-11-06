from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

def start_turtle():
    location = -20
    for turtle in range(0,3):
        turtle = Turtle()
        turtle.color('white')
        turtle.shape('square')
        turtle.penup()
        turtle.goto(x=location, y=0) 
        location += 20

start_turtle()
screen.exitonclick()