from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    model = Column(String)
    color = Column(String)
    price = Column(Integer)
   
   