from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos' #a way for SQLarchemy to know what to name this table

    id = Column(Integer, primary_key=True, index=True) #Demonstrate that this going to be unique, index to increase performance
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)