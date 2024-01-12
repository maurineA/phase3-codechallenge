#car.property
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from .base import Base

engine = create_engine('sqlite:///car_wash.db')
Session = sessionmaker(bind=engine)
session = Session()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    model = Column(String)
    color = Column(String)
    price = Column(Integer)
    clients_id = Column(Integer, ForeignKey('clients.id'))
    employees_id = Column(Integer, ForeignKey('employees.id'))
    
   
    client = relationship("Client" , back_populates='cars')
    employee = relationship("Employee", back_populates='cars')

    #add cars into our db
    @classmethod
    def add_car(self, session, type, model, color, price, clients_id, employees_id):
        new_car = Car(type=type, model=model, color=color, price=price, clients_id=clients_id, employees_id=employees_id)
        session.add(new_car)
        session.commit()


    @classmethod
    def search_car_by_model(cls, session, model):
        return session.query(cls).filter_by(model=model).first()



   