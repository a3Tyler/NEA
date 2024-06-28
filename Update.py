from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

engine = create_engine('sqlite:///user_database.db', echo = True)

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

class Parent(Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True)
    child = relationship("Child", back_populates = "parent")

class Child(Base):
    __tablename__ = "child"

    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True)
    parent = relationship("Parent", back_populates = "child")
    parent_id = Column(Integer, ForeignKey("parent.id"))

parent = Parent(name = "P")

parent.child = [Child(name = "C")]
    
opensession = Session()

print(parent.child[0].name)

opensession.add(parent)
opensession.commit()

opensession.close()