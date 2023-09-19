from tkinter import *
from tkinter import ttk
from functions import spin

root = Tk()

root.geometry("500x500")
root.title("Rock-Paper-Scissors-Game")

choices = ["rock", "paper", "scissors"]

label = Label(root, text="Select your choice", width=20, height=4, font=("calibri", 15))
label.pack()

user_select = ttk.Combobox(root, values=["Rock", "Paper", "Scissors"])
user_select.current(0)
user_select.pack()

button = Button(root, text="Spin", font=("bell mt", 10), command=lambda: spin(user_select.get(), root))
button.pack()

root.mainloop()
