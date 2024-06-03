# # # # # TESTIT CLIENT PROGRAM # # # # #
# Import key functions
from tkinter import *
from re import *
from random import *
from Server import funFindUsername, funCheckPassword, funCheckEmail, funReturnUser, funCreateUser, funSendviaEmail

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
def funLogInCheck(varEmail, varUsername, varPassword):
    # Gets the data from the entries
    email = varEmail.get()
    username = varUsername.get()
    password = varPassword.get()
    
    # Clears the screen
    funClear()

    # Checks if a user has been found
    if funFindUsername(username):
        # Validates the user using the password and email address
        if funCheckPassword(username, password) and funValidateEmail(username, email):
            # Retrieves all of the user's data
            user = funReturnUser(username)

            # Selects the screen to go to based on the type of account
            if user.type == "Teacher":
                TeacherHub(user)
            elif user.type == "Student":
                StudentHub(user)
            else:
                # Displays an error if the user doesn't have either type of account
                txtError = Label(bg = "red", text = "ERROR: user data is invalid. Please ask for support.", font = ("Arial", 24))
                txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                Win.mainloop()
    else:
        # Displays that the user does not exist
        txtError = Label(bg = "red", text = f"ERROR: user with username: '{username}' does not exist", font = ("Arial", 24))
        txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        txtError.after(5000, lambda: LogIn())

# Function that validates and checks the email address
def funValidateEmail(username, email):
    # Creates a variable that represents the standard expression for an email address
    standard_expression = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # Compares the string to the standard expression for an email address
    if fullmatch(standard_expression, email):
        return funCheckEmail(username, email)
    else:
        # Displays that the user does not exist
        txtError = Label(bg = "red", text = "ERROR: email is not valid", font = ("Arial", 24))
        txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        txtError.after(5000, lambda: LogIn())

# Subroutine that sends the data to the database
def funSendDetails(type, varEmail, varUsername, varPassword, varConfirm):
    # Gets the data from the entries
    email = varEmail.get()
    username = varUsername.get()
    password = varPassword.get()
    confirm = varConfirm.get()

    # Clears the screen
    funClear()

    # Compares the passwords
    if password == confirm:
        # Sends the data to the database
        if funCreateUser(type, email, username, password):
            # Goes to authentification
            Authentication(funReturnUser(username))
        else:
            # Displays an error if there is an existing user
            txtError = Label(bg = "red", text = f"ERROR: there is an existing user with username = '{username}'", font = ("Arial", 24))
            txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            txtError.after(5000, lambda: AccountDetails(type))
    else:
        txtError = Label(bg = "red", text = "Please enter the same password for both entries", font = ("Arial", 24))
        txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        txtError.after(5000, lambda: AccountDetails(type))

# Checks the authentication code
def funCheckCode(user, varAuth_code, code, attempts):
    # Gets the inputted code
    input_code = varAuth_code.get()

    # Clears the screen
    funClear()

    # Compares the inputted code to the generated code
    if input_code == code:
        # Edits the account to show that the account is legitimate
        # Selects the screen to go to based on the type of account
        if user.type == "Teacher":
            TeacherHub(user)
        elif user.type == "Student":
            StudentHub(user)
        else:
            # Displays an error if the user doesn't have either type of account
            txtError = Label(bg = "red", text = "ERROR: user data is invalid. Please ask for support.", font = ("Arial", 24))
            txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            Win.mainloop()
    else:
        # Increments the variable 'attempts'
        attempts += 1
        
        # Checks if this is the 3rd time the user has failed
        if attempts % 3 == 0:
            txtError = Label(bg = "red", text = "Code is invalid. Generating a new code...", font = ("Arial", 24))
            txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            txtError.after(5000, lambda: Authentication(user))
        else:
            txtError = Label(bg = "red", text = "Code is invalid", font = ("Arial", 24))
            txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            txtError.after(5000, None)
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
    btnSubmit = Button(width = 15, bg = "green", activebackground = "light green", text = "Submit", font = ("Calibri", 16), command = lambda: funLogInCheck(etrEmail, etrUsername, etrPassword))
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
        # Displays an error if the user has no type
        txtError = Label(bg = "red", text = "ERROR: user has no account type", font = ("Arial", 24))
        txtError.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        txtError.after(5000, lambda: AccountCreation())
    
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
    btnSubmit = Button(width = 15, bg = "green", activebackground = "light green", text = "Submit", font = ("Calibri", 16), command = lambda: funSendDetails(type, etrEmail, etrUsername, etrPassword, etrConfirm))
    btnSubmit.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: AccountCreation())
    btnGo_back.place(relx = 0.01, rely = 0.95)
    
    # Keeps on displaying the screen unless something happens
    Win.mainloop()
# # # # # END # # # # #

# # # # # AUTHENTICATION # # # # #
def Authentication(user):
    # Clears the screen
    funClear()
    
    # Generates a code and sends it via email
    code = randint(1000, 9999)
    funSendviaEmail(user.email, code)
    
    input_code = IntVar()
    attempts = 0
    
    # Creates a label
    txtAuth_title = Label(bg = Win.cget("bg"), text = "Authenticate your account", font = ("Arial", 30))
    txtAuth_title.place(relx = 0.5, rely = 0.05, anchor = CENTER)
    
    # Creates a label
    txtAuth_command = Label(bg = Win.cget("bg"), text = "Enter the 4 digit code that has been sent to the email address", font = ("Arial", 16))
    txtAuth_command.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    
    # Creates an entry box for the user to enter the password
    etrAuth_code = Entry(width = 30, bg = "white", textvariable = input_code, font = ("Calibri", 16))
    etrAuth_code.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    etrAuth_code.insert(0, "Enter password")
    etrAuth_code.bind('<Return>', lambda x: funCheckCode(user, etrAuth_code, code, attempts))
    
    # Creates a button to go back to the prevous screen
    btnGo_back = Button(bg = "dark blue", activebackground = "blue", text = "Go Back", font = ("Calibri", 16), command = lambda: AccountDetails(user.type))
    btnGo_back.place(relx = 0.01, rely = 0.95)

    Win.mainloop()
# # # # # END # # # # #

# # # # # TEACHER HUB # # # # #
def TeacherHub(user):
    print("Yet to start")
# # # # # END # # # # #

# # # # # STUDENT HUB # # # # #
def StudentHub(user):
    print("Yet to start")
# # # # # END # # # # #

# Starts the program
Welcome()

# # # # # END OF PROGRAM # # # # #
