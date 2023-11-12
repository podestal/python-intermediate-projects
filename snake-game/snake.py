from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
location = -20
turtles = []
game_on = True

for turtle in range(0,3):
    turtle = Turtle()
    turtle.color('white')
    turtle.shape('square')
    turtle.penup()
    turtle.goto(x=location, y=0) 
    location += 20
    turtles.append(turtle)

while game_on:
    screen.update()
    time.sleep(0.1)
    for turtle in turtles:
        turtle.forward(20)

screen.exitonclick()