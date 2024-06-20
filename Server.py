# # # # # TESTIT SERVER PROGRAM # # # # #
# Import key functions
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from smtplib import *
from ssl import *
from email.message import EmailMessage
from configparser import ConfigParser

# Create an engine and connect to a SQLite database file (search "SQL Online" and go to first link to find database)
engine = create_engine('sqlite:///testit_user_database.db', echo = False)

# Define a base class for declarative class definitions
Base = declarative_base()

# # # # # USER CLASS # # # # #
class User():
    # Defines the attributes
    def __init__(self, user_id, name, email, password, authentication):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.authentication = authentication
# # # # # END # # # # #

# # # # # TEACHER TABLE # # # # #
class Teacher(Base):
    __tablename__ = 'teachers'
    
    # Table fields
    id = Column(Integer, primary_key = True)
    user_id = Column(String, unique = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    authentication = Column(Boolean)
# # # # # END # # # # #

# # # # # STUDENT TABLE # # # # #
class Student(Base):
    __tablename__ = 'students'
    
    # Table fields
    id = Column(Integer, primary_key = True)
    user_id = Column(String, unique = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    authentication = Column(Boolean)
# # # # # END # # # # #

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session class
Session = sessionmaker(bind = engine)

# # # # # FUNCTIONS # # # # #
# Function that contructs the user id
def funConstructID(type, name):
    # Creates the basic id for the user of that name and account type
    if type == 'Teacher':
        user_id = "T"
    elif type == 'Student':
        user_id = "S"
    
    for i in range(0, len(name) - 1):
        if i == 0:
            user_id = user_id + name[i]
        elif name[i] == " " and (64 < ord(name[i + 1]) < 91):
            user_id = user_id + name[i + 1]
    
    # Finds the first user id that isn't used already
    number = None
    for count in range(1, 1000):
        if count < 10:
            if not funFindUser(user_id + "00" + str(count)):
                number = count
                break
        elif 9 < count < 100:
            if not funFindUser(user_id + "0" + str(count)):
                number = count
                break
        elif 99 < count < 1000:
            if not funFindUser(user_id + str(count)):
                number = count
                break
    print(number)
    
    if not number:
        # Reports that there are too many users with that name and type
        return False
    elif number < 10:
        # Completes the user id
        user_id = user_id + "00" + str(number)
    elif 9 < number < 100:
        # Completes the user id
        user_id = user_id + "0" + str(number)
    elif 99 < number < 100:
        # Completes the user id
        user_id = user_id + str(number)
    
    # Outputs the user id
    return user_id

# Function that creates a user that can be used in the client program
def funConstructUser(user_id, email, password, authentication):
    # Saves the information onto the device by creating variables
    offline_user_id = user_id
    offline_email = email
    offline_password = password
    offline_authentication = authentication
    
    # Constructs a user that can be accessed by the client program
    user = User(offline_user_id, offline_email, offline_password, offline_authentication)
    
    # Sends it back
    return user

# Function that finds the user in the database
def funFindUser(user_id):
    # Creates a session
    session = Session()
    
    if user_id[0] == 'T':
        # Query the teacher table for a user with the given username
        user = session.query(Teacher).filter_by(user_id = user_id).first()
    elif user_id[0] == 'S':
        # Query the student table for a user with the given username
        user = session.query(Student).filter_by(user_id = user_id).first()
    else:
        # Closes the session
        session.close()
        
        return None
    
    if user:
        # Creates a version of the user to be used in the client program
        user = funConstructUser(user.user_id, user.email, user.password, user.authentication)
        
        # Closes the session
        session.close()
        
        return user
    else:
        # Closes the session
        session.close()
        
        return None

# Function that creates a user
def funCreateUser(type, name, email, password):
    # Creates a session
    session = Session()
    
    # Constructs the user id
    user_id = funConstructID(type, name)
    
    if not user_id:
        return False
    
    if user_id[0] == 'T':
        # Creates a new user
        new_user = Teacher(user_id = user_id, name = name, email = email, password = password, authentication = False)

        # Adds the new user to the database
        session.add(new_user)
        session.commit()

        # Creates a version of the user to be used n the client program
        user = funConstructUser(new_user.user_id, new_user.name, new_user.email, new_user.password, new_user.authentication)
        
        # Closes the session
        session.close()
        
        return user
    elif user_id[0] == 'S':
        # Creates a new user
        new_user = Student(user_id = user_id, name = name, email = email, password = password, authentication = False)

        # Adds the new user to the database
        session.add(new_user)
        session.commit()

        # Creates a version of the user to be used n the client program
        user = funConstructUser(new_user.user_id, new_user.name, new_user.email, new_user.password, new_user.authentication)
        
        # Closes the session
        session.close()
        
        return user
    else:
        return False

# Function that removes a user from the database
def funRemoveUser(user_id):
    # Creates a session
    session = Session()

    if user_id[0] == 'T':
        # Finds the user in the database using the id
        user = session.query(Teacher).filter_by(user_id = user_id).first()
    elif user_id[0] == 'S':
        # Finds the user in the database using the id
        user = session.query(Teacher).filter_by(user_id = user_id).first()
    else:
        # Closes the session
        session.close()
        
        # Outputs the error
        return None

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
        return None

# Function that clears the database
def funClearDatabase():
    # Creates a session
    session = Session()

    # Deletes all users until the database is cleared
    Cleared = False
    while not Cleared:
        try:
            # Finds the first user from the database
            user = session.query(Teacher).first()

            # Removes the user from the database
            session.delete(user)
            session.commit()
        except:
            Cleared = True
    
    Cleared = False
    while not Cleared:
        try:
            # Finds the first user from the database
            user = session.query(Student).first()

            # Removes the user from the database
            session.delete(user)
            session.commit()
        except:
            Cleared = True
    
    # Closes the session
    session.close()
    
# Function that sends an email to the email address given
def funSendCodeviaEmail(email, code):
    # Retrieves the credentials
    config = ConfigParser()
    config.read('config.ini')
    config_email = config['Credentials']['email']
    config_password = config['Credentials']['password']
    
    # Creates an message
    message = EmailMessage()
    message.set_content(f"Welcome!\n\nThanks for creating an account with us! Your code is {code}\n\nThis is an automated email. There may be issues with the email contents or the email being sent. Please wait for the issues to be resolved.")
    message['Subject'] = "Log In success"
    message['From'] = config_email
    message['To'] = email

    # Creates a secure SSL context
    context = create_default_context()
    
    # Creates an SMTP server
    server = SMTP_SSL("smtp.gmail.com", port = 465, context = context)
    
    # Logs in to email
    server.login(config_email, config_password)

    # Sends the message
    server.send_message(message)
    
    # Terminates the SMTP server
    server.quit()

# Function that authenticates the user to the database
def funAuthenticateUser(user_id):
    # Creates a session
    session = Session()
    
    # Finds the user in the database
    user = funFindUser(user_id)
    
    # Updates the user authentication status
    user.authentication = True
    
    # Saves the changes
    session.commit()
    
    # Closes the session
    session.close()

# Function that sends an email for the log in
def funSendLogInEmail(email):
    # Retrieves the credentials
    config = ConfigParser()
    config.read('config.ini')
    config_email = config['Credentials']['email']
    config_password = config['Credentials']['password']
    
    # Creates an message
    message = EmailMessage()
    message.set_content(f"Welcome!\n\nYou have now logged into your account! If this wasn't you then please ask for support.\n\nThis is an automated email. There may be issues with the email contents or the email being sent. Please wait for the issues to be resolved.")
    message['Subject'] = "Log In success"
    message['From'] = config_email
    message['To'] = email

    # Creates a secure SSL context
    context = create_default_context()
    
    # Creates an SMTP server
    server = SMTP_SSL("smtp.gmail.com", port = 465, context = context)
    
    # Logs in to email
    server.login(config_email, config_password)

    # Sends the message
    server.send_message(message)
    
    # Terminates the SMTP server
    server.quit()
# # # # # END # # # # #
# # # # # END OF PORGRAM # # # # #