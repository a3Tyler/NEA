# Import key functions
import tkinter
from tkinter import Tk, Frame, Label, Entry, Button, CENTER

# Subroutine that closes the window
def Close():
    exit()

# Subroutine that clears a frame
def Clear():
    for widget in Win.winfo_children():
        widget.destroy()

# Creates a window and sets it's title and makes it fullscreen
Win = Tk()
Win.title("TestIt!")
Win.attributes('-fullscreen', True)

# Creates a button so that the user can exit the program if desired
btnExit = Button(background = "red", text = "X", height = 1, width = 3, command = Close)
btnExit.place(relx = 0.9925, rely = 0.011, anchor = CENTER)

# # # # # WELCOME SCREEN # # # # #
def Welcome():
    # Changes the colour of the background
    Win.config(bg = "light blue")
    
    # Creates a label
    txtWelcome_title = Label(bg = Win.cget("bg"), text = "Welcome to TestIt!", font = ("Arial", 30))
    txtWelcome_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    # Creates a label
    txtWelcome_description = Label(bg = Win.cget("bg"), text = "Test your skills!", font = ("Arial", 16))
    txtWelcome_description.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    # Creates a button that goes to the log in screen
    btnLog_in = Button(width = 15, bg = "#ee5522", activebackground = "#ff7744", text = "Log In", font = ("Calibri", 16), command = LogIn())
    btnLog_in.place(relx = 0.3, rely = 0.5, anchor = CENTER)
    
    # Creates a button that goes to the account creation screen
    btnAccount_creation = Button(width = 15, bg = "green", activebackground = "light green", text = "Create an Account", font = ("Calibri", 16), command = AccountCreation())
    btnAccount_creation.place(relx = 0.7, rely = 0.5, anchor = CENTER)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()

# # # # # LOG IN SCREEN # # # # #
def LogIn():
    print("Yet to start")

# # # # # ACCOUNT CREATION SCREEN # # # # #
def AccountCreation():
    print("Yet to start")

Welcome()