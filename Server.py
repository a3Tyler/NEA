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

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session class
Session = sessionmaker(bind = engine)

# # # # # USER CLASS # # # # #
class User():
    # Defines the attributes
    def __init__(self, user_id, name, email, password, authentication, groups):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.authentication = authentication
        self.groups = groups
# # # # # END # # # # #

# # # # # TEACHER TABLE # # # # #
class Teacher(Base):
    __tablename__ = 'teachers'
    
    # Table fields
    id : Mapped[int] = mapped_column(primary_key = True)
    user_id : Mapped[str] = mapped_column(unique = True)
    name : Mapped[str] = mapped_column()
    email : Mapped[str] = mapped_column()
    password : Mapped[str] = mapped_column()
    authentication : Mapped[str] = mapped_column()
    groups: Mapped[list["Group"]] = relationship(back_populates = "teachers")
# # # # # END # # # # #

# # # # # STUDENT TABLE # # # # #
class Student(Base):
    __tablename__ = 'students'
    
    # Table fields
    id : Mapped[int] = mapped_column(primary_key = True)
    user_id : Mapped[str] = mapped_column(unique = True)
    name : Mapped[str] = mapped_column()
    email : Mapped[str] = mapped_column()
    password : Mapped[str] = mapped_column()
    authentication : Mapped[str] = mapped_column()
    groups: Mapped[list["Group"]] = relationship(back_populates = "students")
# # # # # END # # # # #

# # # # # GROUP TABLE # # # # #
class Group(Base):
    __tablename__ = 'groups'
    
    # Table fields
    id : Mapped[int] = mapped_column(primary_key = True)
    teacher : Mapped["Teacher"] = relationship(back_populates = "groups")
    student : Mapped["Student"] = relationship(back_populates = "groups")
    Grade : Mapped[str] = mapped_column()

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

# Function that finds the user in the database
def funFindUser(user_id):
    # Creates a session
    session = Session()
    
    if user_id[0] == 'T':
        # Query the teacher table for a user with the given username
        user = session.scalars(select(Teacher).where(Teacher.user_id == user_id)).first()
    elif user_id[0] == 'S':
        # Query the student table for a user with the given username
        user = session.scalars(select(Student).where(Student.user_id == user_id)).first()
    else:
        # Closes the session
        session.close()
        
        return None
    
    if user:
        # Creates a version of the user to be used in the client program
        user = User(user.user_id, user.name, user.email, user.password, user.authentication)
        
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
    elif user_id[0] == 'T':
        # Creates a new user and adds the new user to the database
        new_user = session.scalars(insert(Teacher).returning(Teacher), {user_id, name, email, password, False})

        # Creates a version of the user to be used n the client program
        user = User(new_user.user_id, new_user.name, new_user.email, new_user.password, new_user.authentication)
        
        # Closes the session
        session.close()
        
        return user
    elif user_id[0] == 'S':
        # Creates a new user and adds the new user to the database
        new_user = session.scalars(insert(Student).returning(Student), {user_id, name, email, password, False})

        # Creates a version of the user to be used n the client program
        user = User(new_user.user_id, new_user.name, new_user.email, new_user.password, new_user.authentication)
        
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
        # Removes the user from the database
        try:
            session.execute(delete(Teacher).where(Teacher.user_id == user_id))
        except:
            pass
    elif user_id[0] == 'S':
        # Removes the user from the database
        try:
            session.execute(delete(Student).where(Student.user_id == user_id))
        except:
            pass

    # Closes the session
    session.close()

# Function that clears the database
def funClearDatabase():
    # Creates a session
    session = Session()

    # Deletes all data in the database
    session.execute(delete(Group))
    session.execute(delete(Teacher))
    session.execute(delete(Student))
    
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
    
    # Updates the user authentication status
    if user_id[0] == 'T':
        session.execute(update(Teacher).where(Teacher.user_id == user_id).values(authentication = True))
    elif user_id[0] == 'S':
        session.execute(update(Student).where(Student.user_id == user_id).values(authentication = True))
    
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