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
    
    def add_employee(self, name, contact):
        new_employee = Employee(name=name, contact=contact)
        session.add(new_employee)
        session.commit()

    #search employees
    def search_employee(self, name):
        employee = session.query(Employee).filter_by(name=name).first()
        return print(f"found employee named {employee.name} with contact: {employee.contact}")
    
    
    #delete employee
    def delete_employee(self, name):
        employees = session.query(Employee).filter_by(name=name).first()
        
        if employees:
            session.delete(employees)
            session.commit()
            print(f"employee with the name {name} deleted successfully")

        else:
            print(f"employee with name {name} not found")

    

    