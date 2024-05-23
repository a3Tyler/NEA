# # # # # TESTIT CLIENT PROGRAM # # # # #
# Import key functions
from tkinter import *
from re import *

# # # # # SUBROUTINES & FUNCTIONS # # # # #
# Subroutine that closes the window
def funClose():
    exit()

# Subroutine that clears the frame
def funClear():
    for widget in Win.winfo_children():
        if widget != btnExit:
            widget.destroy()

# Subroutine that sets the text to default
def funSetText(widget, text_variable, text, hide):
    if text_variable.get() == "":
        if not hide:
            widget.config(show = "")
        else:
            widget.config(show = "*")
        widget.insert(0, text)

# Subroutine that clears the text
def funClearText(widget, text_variable, default_text, hide):
    if text_variable.get() == default_text:
        if not hide:
            widget.config(show = "")
        else:
            widget.config(show = "*")
        widget.delete(0, END)

# Subroutine that checks the database to validate the user
def funLogInCheck(email, username, password):
    # Finds the user in the database using the username
    user_id = funFindUsername(username)

    # Checks if a user has been found
    if user_id == None:
        print("ERROR: 'username' not found in database")
        funClose()
    else:
        # Validates the user using the password and email address
        if funCheckPassword(password, user_id) and funValidateEmail(email, user_id):
            print("Yet to start")

# Function that finds the username in a database
def funFindUsername(username):
    print("Yet to start")

# Function that checks the password
def funCheckPassword(password, user_id):
    print("Yet to start")

# Function that validates and checks the email address
def funValidateEmail(email, user_id):
    # Creates a variable that represents the standard expression for an email address
    standard_expression = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # Compares the string to the standard expression for an email address
    if fullmatch(standard_expression, email):
        # Compares it to the user's email address in the database
        print("Yet to start")
    else:
        return False

# Subroutine that sends the data to the database
def funSendDetails(email, username, password, confirm):
    print("Yet to start")
# # # # # END # # # # #

# Creates a window and sets it's title and makes it fullscreen
Win = Tk()
Win.title("TestIt!")
Win.attributes('-fullscreen', True)

# Creates a button so that the user can exit the program if desired
btnExit = Button(background = "red", text = "X", height = 1, width = 3, command = lambda: funClose())
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
# # # # # END # # # # #

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
    etrEmail.bind('<FocusOut>', lambda x: funSetText(etrEmail, email, "Enter email", False))
    etrEmail.bind('<FocusIn>', lambda x: funClearText(etrEmail, email, "Enter email", False))
    
    # Creates an entry box for the user to enter the username
    etrUsername = Entry(width = 30, bg = "white", textvariable = username, font = ("Calibri", 16))
    etrUsername.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    etrUsername.insert(0, "Enter username")
    etrUsername.bind('<FocusOut>', lambda x: funSetText(etrUsername, username, "Enter username", False))
    etrUsername.bind('<FocusIn>', lambda x: funClearText(etrUsername, username, "Enter username", False))
    
    # Creates an entry box for the user to enter the password
    etrPassword = Entry(width = 30, bg = "white", textvariable = password, font = ("Calibri", 16))
    etrPassword.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    etrPassword.insert(0, "Enter password")
    etrPassword.bind('<FocusOut>', lambda x: funSetText(etrPassword, password, "Enter password", False))
    etrPassword.bind('<FocusIn>', lambda x: funClearText(etrPassword, password, "Enter password", True))
    
    # Creates a button that submits the data
    btnSubmit = Button(width = 15, bg = "green", activebackground = "light green", text = "Submit", font = ("Calibri", 16), command = lambda: funLogInCheck(email, username, password))
    btnSubmit.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: Welcome())
    btnGo_back.place(relx = 0.01, rely = 0.95)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()
# # # # # END # # # # #

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
# # # # # END # # # # #

# # # # # ACCOUNT DETAILS SCREEN # # # # #
def AccountDetails(type):
    # Clears the screen
    funClear()
    
    # Declares important variables
    email = StringVar()
    username = StringVar()
    password = StringVar()
    confirm = StringVar()

    # Changes the colour of the background
    if type == "Teacher":
        Win.config(bg = "blue")
    elif type == "Student":
        Win.config(bg = "green")
    else:
        print("ERROR: No 'type' for Account")
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
    etrEmail.insert(0, "Enter email")
    etrEmail.bind('<FocusOut>', lambda x: funSetText(etrEmail, email, "Enter email", False))
    etrEmail.bind('<FocusIn>', lambda x: funClearText(etrEmail, email, "Enter email", False))
    
    # Creates an entry box for the user to enter the username
    etrUsername = Entry(width = 30, bg = "white", textvariable = username, font = ("Calibri", 16))
    etrUsername.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    etrUsername.insert(0, "Enter username")
    etrUsername.bind('<FocusOut>', lambda x: funSetText(etrUsername, username, "Enter username", False))
    etrUsername.bind('<FocusIn>', lambda x: funClearText(etrUsername, username, "Enter username", False))
    
    # Creates an entry box for the user to enter the password
    etrPassword = Entry(width = 30, bg = "white", textvariable = password, font = ("Calibri", 16))
    etrPassword.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    etrPassword.insert(0, "Enter password")
    etrPassword.bind('<FocusOut>', lambda x: funSetText(etrPassword, password, "Enter password", False))
    etrPassword.bind('<FocusIn>', lambda x: funClearText(etrPassword, password, "Enter password", True))
    
    # Creates an entry box for the user to re-enter the password
    etrConfirm = Entry(width = 30, bg = "white", textvariable = confirm, font = ("Calibri", 16))
    etrConfirm.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    etrConfirm.insert(0, "Enter password again")
    etrConfirm.bind('<FocusOut>', lambda x: funSetText(etrConfirm, confirm, "Enter password again", False))
    etrConfirm.bind('<FocusIn>', lambda x: funClearText(etrConfirm, confirm, "Enter password again", True))
    
    # Creates a button that submits the data
    btnSubmit = Button(width = 15, bg = "green", activebackground = "light green", text = "Submit", font = ("Calibri", 16), command = lambda: funSendDetails(email, username, password, confirm))
    btnSubmit.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: AccountCreation())
    btnGo_back.place(relx = 0.01, rely = 0.95)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()
# # # # # END # # # # #

Welcome()
# # # # # END OF PROGRAM # # # # #