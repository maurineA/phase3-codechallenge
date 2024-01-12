#seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.car import Car
from modules.client import Client
from modules.employee import Employee
from modules.base import Base

engine = create_engine('sqlite:///car_wash.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample data for employees
employee1 = Employee(name='John Doe', contact=123456789)
employee2 = Employee(name='Jane Smith', contact=987654321)

# Sample data for clients
client1 = Client(contact=111223344, name='Client A')
client2 = Client(contact=555666777, name='Client B')

# Sample data for cars
car1 = Car(type='Sedan', model='Toyota Camry', color='Blue', price=25000, clients_id=3, employees_id=1)
car2 = Car(type='SUV', model='Honda CR-V', color='Red', price=30000, clients_id=4, employees_id=2)

# Add the sample data to the session
session.add_all([employee1, employee2, client1, client2, car1, car2])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
