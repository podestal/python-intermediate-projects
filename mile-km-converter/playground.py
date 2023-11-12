# import tkinter

# window = tkinter.Tk()
# window.title('My First GUI')
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
# my_label.pack(side='left')


# window.mainloop()

# Positional Argumens

# def add(*args):
#     added = 0
#     for n in args:
#         added += n
#     print(added)

# add(1, 3, 6, 10, 16)

# Keyword Arguments

def calcuate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(value)
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calcuate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Toyota')
print(my_car.make)
print(my_car.model)
