from tkinter import *
from tkinter import ttk
from random import *

root = Tk()

root.geometry("500x500")
root.title("Rock-Paper-Scissors-Game")

choices = ["rock", "paper", "scissors"]
choose_number = randint(0, 2)

label = Label(root, text="Select your choice", width=20, height=4, font=("calibri", 15))
label.pack()

user_select = ttk.Combobox(root, values=["Rock", "Paper", "Scissors"])
user_select.current(0)
user_select.pack()

wl_label = Label(root, text="", font=("arial", 10), width=50, height=4)
wl_label.pack()
button = Button(root, text="Spin", font=("bell mt", 10), command=spin)
button.pack()

root.mainloop()
