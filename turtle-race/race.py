from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.pensize(10)

def move_forward():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.exitonclick()