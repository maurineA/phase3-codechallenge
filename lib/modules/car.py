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
    clients_id = Column(Integer)
    employees_id = Column(Integer)
   
    clients = relationship("Client" , back_populates='cars')
    employees = relationship("Employee", back_populates='cars')

    #add cars into our db
    @classmethod
    def add_car(cls, session, type, model, color, price, clients_id, employees_id):
        new_car = cls(type=type, model=model, color=color, price=price, clients_id=clients_id, employees_id=employees_id)
        session.add(new_car)
        session.commit()



   