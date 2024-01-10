from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(Integer)
    cars_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car', back_populates='car')