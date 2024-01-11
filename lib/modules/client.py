from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Client(Base):
    __tablename__ ='clients'

    id = Column(Integer, primary_key=True)
    contact = Column(Integer)
    name = Column(String)
    cars_id = Column(Integer, ForeignKey('cars.id'))
    
    cars = relationship('Car', back_populates='clients')