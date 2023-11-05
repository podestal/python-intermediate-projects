# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()

# def move_forward():
#     t.forward(10)

# def move_backwards():
#     t.backward(10)

# def turn_left():
#     new_heading = t.heading() + 10
#     t.setheading(new_heading)

# def turn_right():
#     new_heading = t.heading() - 10
#     t.setheading(new_heading)

# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()

# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(move_backwards, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear, 'c')
# screen.exitonclick()

from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
list_of_turtles = []
race_on = True

y_axis = -90

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_axis)
    new_turtle.color(color)
    y_axis += 30
    list_of_turtles.append(new_turtle)

while race_on:
    for turtle in list_of_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('you win')
            else:
                print('you lose')
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
