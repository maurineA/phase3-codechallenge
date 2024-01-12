from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(Integer)
    cars_id = Column(Integer, ForeignKey('cars.id'))
    cars = relationship('Car', back_populates='employees')

    #adding employees into the our db
    @classmethod
    def add_employee(cls, session, name, contact, cars_id):
        new_employee = cls(name=name, contact=contact, cars_id=cars_id)
        session.add(new_employee)
        session.command()

    #search employees
    @classmethod
    def search_employee(cls, session, name):
        return session.query(cls).filter_by(name=name).first()