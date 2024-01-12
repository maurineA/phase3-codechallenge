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

    
    def search_client_by_name(self, name):
        client = session.query(Client).filter_by(name=name).first()
        return print(f"found client named {client.name} with contact: {client.contact}")
    
    #delete client
    def delete_client(self, name):
        clients = session.query(Client).filter_by(name=name).first()
        
        if clients:
            session.delete(clients)
            session.commit()
            print(f"client with the name {name} deleted successfully")

        else:
            print(f"client with name {name} not found")
        
    
