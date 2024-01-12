from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Client(Base):
    __tablename__ ='clients'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    contact = Column(Integer)
    cars_id = Column(Integer, ForeignKey('cars.id'))
    
    cars = relationship('Car', back_populates='clients')

    @classmethod
    def add_client(cls, session, name, cars_id, contact ):
        new_client = cls(name=name, contact=contact, cars_id=cars_id)
        session.add(new_client)
        session.commit()