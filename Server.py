# # # # # TESTIT SERVER PROGRAM # # # # #
# Import key functions
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

# Create an engine and connect to a SQLite database file (search "SQL Online" and go to first link to find database)
engine = create_engine('sqlite:///testit_user_database.db', echo=False)

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