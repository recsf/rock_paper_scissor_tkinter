from random import randint
from tkinter.messagebox import showinfo


def spin(value, root):
    choose_number = randint(0, 2)
    human = 0
    if value == "Rock":
        human = 0
    elif value == "Paper":
        human = 1
    elif value == "Scissors":
        human = 2
    if human == 0:
        if choose_number == 0:
            showinfo("", "Tie! - "+" Computer: Bad luck")
        elif choose_number == 1:
            showinfo("", "YOU Loose - "+" Computer: I am better")
        elif choose_number == 2:
            showinfo("", "YOU Won - "+" Computer: You won by luck")
    elif human == 1:
        if choose_number == 1:
            showinfo("", "Tie! - "+" Computer: Bad luck")
        elif choose_number == 0:
            showinfo("", "YOU Loose - "+" Computer: I am better")
        elif choose_number == 2:
            showinfo("", "YOU Won - "+" Computer: You won by luck")
    elif human == 2:
        if choose_number == 2:
            showinfo("", "Tie! - "+" Computer: Bad luck")
        elif choose_number == 0:
            showinfo("", "YOU Loose - "+" Computer: I am better")
        elif choose_number == 1:
            showinfo("", "YOU Won - "+" Computer: You won by luck")
