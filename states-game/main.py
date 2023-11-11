import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)



data = pd.read_csv('50_states.csv')
states_list = data['state'].to_list()
x_coor_list = data['x'].to_list()
y_coor_list = data['y'].to_list()
states_guessed = []


while len(states_guessed) < 50:
    answer_state = screen.textinput(title=str(len(states_guessed)) + '/50 States Correct', prompt='What is another name of state').title()
    if answer_state in states_list and answer_state not in states_guessed:
        idx = states_list.index(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_coor_list[idx]),int(y_coor_list[idx]))
        t.write(answer_state)
        states_guessed.append(answer_state)


screen.exitonclick()

