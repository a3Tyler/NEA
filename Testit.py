# This file contains the code for TestIt! (my NEA project)

# Import key functions
import tkinter
from tkinter import Tk, Label, Entry, Button, CENTER

# Creates a title
Title = Tk()
Title.title("TestIt!")

# Subroutine that changes the size of text when the window size changes
def resize(e):
    global txtWelcome_title
    size = e.width/10
    txtWelcome_title.config(font = ("Arial", int(round(e.height/20))))

# Subroutine that displays the Welcome screen
def Welcome():
    global txtWelcome_title
    txtWelcome_title = tkinter.Label(text = "Welcome to TestIt!", font = ("Arial", 21))
    txtWelcome_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    Title.bind('<Configure>', resize)
    Title.mainloop()

Welcome()