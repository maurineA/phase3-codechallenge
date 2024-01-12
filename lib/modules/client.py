#client.property
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from .base import Base

engine = create_engine('sqlite:///car_wash.db')
Session = sessionmaker(bind=engine)
session = Session()

class Client(Base):
    __tablename__ ='clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(Integer)
    
    
    cars = relationship("Car", back_populates="client")

    
    def add_client(self,name, contact ):
        new_client = Client(name=name, contact=contact)
        session.add(new_client)
        session.commit()

    @classmethod
    def search_client_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).first()