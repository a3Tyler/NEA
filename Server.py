# # # # # TESTIT SERVER PROGRAM # # # # #
# Import key functions
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from smtplib import *
from ssl import *
from email.message import EmailMessage

# Create an engine and connect to a SQLite database file (search "SQL Online" and go to first link to find database)
engine = create_engine('sqlite:///testit_user_database.db', echo = False)

# Define a base class for declarative class definitions
Base = declarative_base()

# # # # # USER TABLE # # # # #
class User(Base):
    __tablename__ = 'users'
    
    # Table fields
    id = Column(Integer, primary_key = True)
    type = Column(String)
    email = Column(String)
    username = Column(String, unique = True)
    password = Column(String)
    authentication = Column(Boolean)
# # # # # END # # # # #

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session class
Session = sessionmaker(bind = engine)

# # # # # FUNCTIONS # # # # #
# Function checks if the username exists in the database
def funFindUsername(username):
    # Creates a session
    session = Session()
    
    # Query the database for a user with the given username
    user = session.query(User).filter_by(username = username).first()
    
    # Closes the session
    session.close()
    
    # Returns if the username has been found in the databse
    if user:
        return True
    else:
        return False

# Function that checks if the inputted password is correct
def funCheckPassword(username, input_password):
    # Creates a session
    session = Session()
    
    # Query the database for the user with the given username
    user = session.query(User).filter_by(username = username).first()
    
    # Closes the session
    session.close()
    
    # Compares the inputted password to the user's password and returns the result
    return input_password == user.password

# Function that checks if the inputted email address is correct
def funCheckEmail(username, input_email):
    # Creates a session
    session = Session()
    
    # Query the database for the user with the given username
    user = session.query(User).filter_by(username = username).first()
    
    # Closes the session
    session.close()

    # Compares the inputted password to the user's password and returns the result
    return input_email == user.email

# Function that returns all of the user's data
def funReturnUser(username):
    # Creates a session
    session = Session()

    # Query the database for the user with the given username
    user = session.query(User).filter_by(username = username).first()

    # Returns the user
    return user

# Function that creates a user
def funCreateUser(type, email, username, password):
    # Creates a session
    session = Session()

    # Checks if there is an existing user
    existing_user = session.query(User).filter_by(username = username).first()
    if existing_user:
        # Closes the session
        session.close()
        return False
    else:
        # Creates a new user
        new_user = User(type = type, email = email, username = username, password = password, authentication = False)

        # Adds the new user to the database
        session.add(new_user)
        session.commit()

        # Closes the session
        session.close()
        return True

# Removes a user from the database
def funRemoveUser(id):
    # Creates a session
    session = Session()

    # Finds the user in the database using the id
    user = session.query(User).filter_by(id = id).first()

    # Checks that a user has been found
    if user:
        # Removes the user from the database
        session.delete(user)
        session.commit()

        # Closes the session
        session.close()
    else:
        # Closes the session
        session.close()

        # Outputs the error
        print(f"ERROR: no user with id = {id}")

# Clears the database
def funClearDatabase():
    # Creates a session
    session = Session()

    # Deletes all users until the database is cleared
    Cleared = False
    while not Cleared:
        try:
            # Finds the first user from the database
            user = session.query(User).first()

            # Removes the user from the database
            session.delete(user)
            session.commit()
        except:
            Cleared = True
    
    # Closes the session
    session.close()
    
# Sends an email to the email address given
def funSendviaEmail(email, code):
    # Creates an message
    message = EmailMessage()
    message.set_content(f"Welcome!\n\nThanks for setting up an account with us! Enter the authentication code below so that you can confirm that you are a legitimate user.\n\nYour code is: {code}\n\nThis is an automated email. There may be issues with the email contents or the email being sent. Please wait for the issues to be resolved.")
    message['Subject'] = "Authentication"
    message['From'] = "testitauthentication@gmail.com"
    message['To'] = email

    # Create a secure SSL context
    context = create_default_context()
    
    # Create an SMTP server
    server = SMTP_SSL("smtp.gmail.com", port = 465, context = context)
    
    # Send the message
    server.send_message(message)
    
    # Terminate the SMTP server
    server.quit()
# # # # # END # # # # #
# # # # # END OF PORGRAM # # # # #
