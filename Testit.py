# Import key functions
import tkinter
from tkinter import Tk, Frame, Label, Entry, Button, StringVar, CENTER

# Subroutine that closes the window
def funClose():
    exit()

# Subroutine that clears the frame
def funClear():
    for widget in Win.winfo_children():
        if widget != btnExit:
            widget.destroy()

# Subroutine that sets the text to default
def funSetText(widget, text_variable, text, show):
    if text_variable.get() == "":
        widget.insert(0, text)
        widget.config(show = show)

# Subroutine that clears the text
def funClearText(widget, text_variable, default_text, show):
    if text_variable.get() == default_text:
        widget.delete(0, "end")
        widget.config(show = show)

# Creates a window and sets it's title and makes it fullscreen
Win = Tk()
Win.title("TestIt!")
Win.attributes('-fullscreen', True)

# Creates a button so that the user can exit the program if desired
btnExit = Button(background = "red", text = "X", height = 1, width = 3, command = funClose)
btnExit.place(relx = 0.99, rely = 0.015, anchor = CENTER)

# # # # # WELCOME SCREEN # # # # #
def Welcome():
    # Clears the screen
    funClear()
    
    # Changes the colour of the background
    Win.config(bg = "light blue")
    
    # Creates a label
    txtWelcome_title = Label(bg = Win.cget("bg"), text = "Welcome to TestIt!", font = ("Arial", 30))
    txtWelcome_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    # Creates a label
    txtWelcome_description = Label(bg = Win.cget("bg"), text = "Test your skills!", font = ("Arial", 16))
    txtWelcome_description.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    # Creates a button that goes to the Log In screen
    btnLog_in = Button(width = 15, bg = "#ee5522", activebackground = "#ff7744", text = "Log In", font = ("Calibri", 16), command = lambda: LogIn())
    btnLog_in.place(relx = 0.3, rely = 0.5, anchor = CENTER)
    
    # Creates a button that goes to the Account Creation screen
    btnAccount_creation = Button(width = 15, bg = "green", activebackground = "light green", text = "Create an Account", font = ("Calibri", 16), command = lambda: AccountCreation())
    btnAccount_creation.place(relx = 0.7, rely = 0.5, anchor = CENTER)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()

# # # # # LOG IN SCREEN # # # # #
def LogIn():
    # Clears the screen
    funClear()
    
    # Declares important variables
    email = StringVar()
    username = StringVar()
    password = StringVar()

    # Changes the colour of the background
    Win.config(bg = "light blue")
    
    # Creates a label
    txtLogIn_title = Label(bg = Win.cget("bg"), text = "Welcome Back!", font = ("Arial", 30))
    txtLogIn_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    # Creates a label
    txtLogIn_command = Label(bg = Win.cget("bg"), text = "Enter your email, username and password below", font = ("Arial", 16))
    txtLogIn_command.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    # Creates an entry box for the user to enter the email address
    etrEmail = Entry(width = 30, bg = "white", textvariable = email, font = ("Calibri", 16))
    etrEmail.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    etrEmail.insert(0, "Enter email")
    etrEmail.bind('<FocusIn>', funSetText(etrEmail, email, "Enter email", None))
    etrEmail.bind('<FocusOut>', funClearText(etrEmail, email, "Enter email", None))
    
    # Creates an entry box for the user to enter the username
    etrUsername = Entry(width = 30, bg = "white", textvariable = username, font = ("Calibri", 16))
    etrUsername.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    etrUsername.insert(0, "Enter username")
    etrUsername.bind('<FocusIn>', funSetText(etrUsername, username, "Enter username", None))
    etrUsername.bind('<FocusOut>', funClearText(etrUsername, username, "Enter username", None))
    
    # Creates an entry box for the user to enter the password
    etrPassword = Entry(width = 30, bg = "white", textvariable = password, show = None, font = ("Calibri", 16))
    etrPassword.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    etrPassword.insert(0, "Enter password")
    etrPassword.bind('<FocusIn>', funSetText(etrPassword, password, "Enter password", None))
    etrPassword.bind('<FocusOut>', funClearText(etrPassword, password, "Enter password", "*"))
    
    # Creates a button that submits the data
    btnSubmit = Button(width = 15, bg = "green", activebackground = "light green", text = "Submit", font = ("Calibri", 16), command = lambda: LogInCheck(email, username, password))
    btnSubmit.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: Welcome())
    btnGo_back.place(relx = 0.01, rely = 0.95)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()

# Subroutine that checks the database to validate the user
def LogInCheck(email, username, password):
    print("Yet to start")

# # # # # ACCOUNT CREATION SCREEN # # # # #
def AccountCreation():
    # Clears the screen
    funClear()

    # Changes the colour of the background
    Win.config(bg = "light blue")
    
    # Creates a label
    txtCreation_title = Label(bg = Win.cget("bg"), text = "Create an Account", font = ("Arial", 30))
    txtCreation_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    # Creates a label
    txtCreation_question = Label(bg = Win.cget("bg"), text = "Teacher or Student?", font = ("Arial", 16))
    txtCreation_question.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    # Creates a button that sets the account type as "Teacher" and goes to the Account Details screen
    btnTeacher = Button(width = 15, bg = "dark blue", activebackground = "blue", text = "Teacher", font = ("Calibri", 16), command = lambda: AccountDetails("Teacher"))
    btnTeacher.place(relx = 0.3, rely = 0.5, anchor = CENTER)
    
    # Creates a button that sets the account type as "Student" and goes to the Account Details screen
    btnStudent = Button(width = 15, bg = "green", activebackground = "light green", text = "Student", font = ("Calibri", 16), command = lambda: AccountDetails("Student"))
    btnStudent.place(relx = 0.7, rely = 0.5, anchor = CENTER)
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: Welcome())
    btnGo_back.place(relx = 0.01, rely = 0.95)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()

# # # # # ACCOUNT DETAILS SCREEN # # # # #
def AccountDetails(Type):
    # Clears the screen
    funClear()
    
    # Declares important variables
    email = None
    username = None
    password = None
    confirm = None

    # Changes the colour of the background
    if Type == "Teacher":
        Win.config(bg = "blue")
    elif Type == "Student":
        Win.config(bg = "green")
    else:
        print("ERROR: No 'Type' for Account")
        funClose()
    
    # Creates a label
    txtCreation_title = Label(bg = Win.cget("bg"), text = "Create an Account", font = ("Arial", 30))
    txtCreation_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    # Creates a label
    txtCreation_command = Label(bg = Win.cget("bg"), text = "Enter your email, username and password below", font = ("Arial", 16))
    txtCreation_command.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    # Creates an entry box for the user to enter the email address
    etrEmail = Entry(width = 30, bg = "white",  textvariable = email, font = ("Calibri", 16))
    etrEmail.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    # Creates an entry box for the user to enter the username
    etrUsername = Entry(width = 30, bg = "white", textvariable = username, font = ("Calibri", 16))
    etrUsername.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    # Creates an entry box for the user to enter the password
    etrPassword = Entry(width = 30, bg = "white", textvariable = password, font = ("Calibri", 16))
    etrPassword.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    # Creates an entry box for the user to re-enter the password
    etrConfirm = Entry(width = 30, bg = "white", textvariable = confirm, show = "*", font = ("Calibri", 16))
    etrConfirm.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    # Creates a button that submits the data
    btnSubmit = Button(width = 15, bg = "green", activebackground = "light green", text = "Submit", font = ("Calibri", 16), command = lambda: SendDetails(email, username, password, confirm))
    btnSubmit.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: AccountCreation())
    btnGo_back.place(relx = 0.01, rely = 0.95)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()

# Subroutine that sends the data to the database
def SendDetails(email, username, password, confirm):
    print("Yet to start")

Welcome()