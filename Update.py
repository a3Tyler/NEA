from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

engine = create_engine('sqlite:///user_database.db', pool_pre_ping = True, echo = False)

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

class Parent(Base):
    __tablename__ = 'Parent'
    
    # Table fields
    id : Mapped[int] = mapped_column(primary_key = True)
    age : Mapped[int] = mapped_column()
    name : Mapped[str] = mapped_column()
    children : Mapped[list["Child"]] = mapped_column(ForeignKey("Child.id"))

class Child(Base):
    __tablename__ = 'Child'
    
    # Table fields
    id : Mapped[int] = mapped_column(primary_key = True)
    age : Mapped[int] = mapped_column()
    name : Mapped[str] = mapped_column()
    parent : Mapped["Parent"] = mapped_column(ForeignKey("Parent.id"))
    
opensession = Session()

result = opensession.execute(select(Parent).order_by(Parent.id))
print(result)

opensession.close()