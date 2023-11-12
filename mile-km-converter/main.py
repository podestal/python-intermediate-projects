from tkinter import *

window = Tk()
window.title('Miles to Kilometer Converter')

def converter():
    kms = round(int(miles_input.get()) * 1.609, 2)
    kilometer_result_label.config(text=str(kms))

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_qeual_label = Label(text='is equal to')
is_qeual_label.grid(column=0,row=1)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text='Calculate', command=converter)
calculate_button.grid(column=1,row=2)

window.mainloop()