#employee.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from .base import Base

engine = create_engine('sqlite:///car_wash.db')
Session = sessionmaker(bind=engine)
session = Session()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(Integer)
    
    cars = relationship('Car', back_populates='employee')

    #adding employees into the our db
    @classmethod
    def add_employee(cls, session, name, contact):
        new_employee = cls(name=name, contact=contact)
        session.add(new_employee)
        session.commit()

    #search employees
    @classmethod
    def search_employee(cls, session, name):
        return session.query(cls).filter_by(name=name).first()