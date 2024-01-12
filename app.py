from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from lib.modules.client import Client
from lib.modules.car import Car
from lib.modules.employee import Employee

import click

engine = create_engine('sqlite:///car_wash.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@click.group()
def cli():
    pass

#added hello test word to the cli group
@cli.command()  
def hello():
    click.echo("hello maurine")


#add client cli command
@cli.command()
def add_client():
    Session =SessionLocal()
    name = input("Enter client's name: ")
    contact = int(input("Enter client's contact: "))
    cars = Session.query(Car).all()
    click.echo("Available cars:")
    for car in cars:
        click.echo(f"{car.id}: {car.model}")
    cars_id = int(input("Enter car's ID: "))
    
    add_client = Client(name=name, contact=contact, cars_id=cars_id)
    Session.add(add_client)
    Session.commit()
    click.echo("Client added successfully!")
    Session.close()


#add car cli command
@cli.command()
def add_car():
    Session = SessionLocal()
    type = input("Enter car type: ")
    model = input("Enter car model: ")
    color = input("Enter car color: ")
    price = int(input("Enter car price: "))
    clients = Session.query(Client).all()
    click.echo("Available Clients:")
    for client in clients:
        click.echo(f"{client.id}: {client.name}")
    clients_id = int(input("Enter client's ID: "))

    employees = Session.query(Employee).all()
    click.echo("Available Employees:")
    for employee in employees:
        click.echo(f"{employee.id}: {employee.name}")
    employees_id = int(input("Enter employee's ID: "))

    new_car = Car(type=type, model=model, color=color, price=price, clients_id=clients_id, employees_id=employees_id)
    Session.add_data(new_car)
    Session.commit()
    click.echo("Car added successfully!")
    Session.close()


#added add_employee to the cli group
@cli.command()  
def add_employee():
    Session = SessionLocal()
    name = input("Enter Employee's name: ")
    contact = int(input("Enter Employees phone number: "))
    cars = Session.query(Car).all()
    click.echo("Available cars:")
    for car in cars:
        click.echo(f"{car.id}: {car.model}")

    cars_id = int(input("Enter car's ID: "))

    new_employee = Employee(name=name, contact=contact, cars_id=cars_id)
    Session.add(new_employee)
    Session.commit()
    click.echo("Employee added successfully")
    Session.close()

@cli.command()
def search_client():
    Session = SessionLocal()
    name = input("Enter client's name: ")
    result = Session.query(Client).filter_by(name=name).first()
    if result:
        click.echo(f"Client found: {result.name}")
    else:
        click.echo(f"Client with name '{name}' not found.")
    Session.close()
    
@click.command()
def search_car():
    Session = SessionLocal()
    model = input("Enter car model: ")
    result = Session.query(Car).filter_by(model=model).first()
    if result:
        click.echo(f"Car found: {result.model}")
    else:
        click.echo(f"Car with model '{model}' not found.")
    Session.close()


@click.command()
def search_employee():
    session = SessionLocal()
    name = input("Enter employee's name: ")
    result = session.query(Employee).filter_by(name=name).first()
    if result:
        click.echo(f"Employee found: {result.name}")
    else:
        click.echo(f"Employee with name '{name}' not found.")
    session.close()







cli.add_command(hello)
cli.add_command(add_client)
cli.add_command(add_car)
cli.add_command(add_employee)
cli.add_command(search_client)
cli.add_command(search_car)
cli.add_command(search_employee)




if __name__ == '__main__':
    cli()
