#app.property
# from sqlalchemy.orm import Session, sessionmaker
# from sqlalchemy import create_engine
from modules.client import Client
from modules.car import Car
from modules.employee import Employee

import click


@click.group()
def cli():
    pass
clients = Client()
#added hello test word to the cli group
@cli.command()  
def hello():
    click.echo("hello maurine")


#add client cli command
@cli.command()
@click.option('--name',prompt="Enter client's name", help="Enter client's name")
@click.option('--contact',prompt="Enter client's contact", help="Enter client's contact")
def add_client(name, contact):
    
    # name = input("Enter client's name: ")
    # contact = int(input("Enter client's contact: "))

    
    clients.add_client(name, contact)
   
    click.echo("Client added successfully!")
    


@cli.command()
@click.option('--type', prompt="Enter car type", help="Enter car type")
@click.option('--model', prompt="Enter car model", help="Enter car model")
@click.option('--color', prompt="Enter car color", help="Enter car color")
@click.option('--price', type=int, prompt="Enter car price", help="Enter car price")
@click.option('--client-id', type=int, prompt="Enter client's ID", help="Enter client's ID")
@click.option('--employee-id', type=int, prompt="Enter employee's ID", help="Enter employee's ID")
def add_car(type, model, color, price, client_id, employee_id):
    client = Client.query.get(client_id)
    employee = Employee.query.get(employee_id)

    if not client:
        click.echo(f"Client with ID {client_id} not found.")
        return

    if not employee:
        click.echo(f"Employee with ID {employee_id} not found.")
        return

    Car.add_car(type, model, color, price, client.id, employee.id)
    click.echo("Car added successfully!")




# #added add_employee to the cli group
# @cli.command()  
# def add_employee():
#     Session = SessionLocal()
#     name = input("Enter Employee's name: ")
#     contact = int(input("Enter Employees phone number: "))
#     # cars = Session.query(Car).all()
#     # click.echo("Available cars:")
#     # for car in cars:
#     #     click.echo(f"{car.id}: {car.model}")

#     # cars_id = int(input("Enter car's ID: "))

#     new_employee = Employee(name=name, contact=contact)
#     Session.add(new_employee)
#     Session.commit()
#     click.echo("Employee added successfully")
#     Session.close()

# @cli.command()
# def search_client():
#     Session = SessionLocal()
#     name = input("Enter client's name: ")
#     result = Session.query(Client).filter_by(name=name).first()
#     if result:
#         click.echo(f"Client found: {result.name}")
#     else:
#         click.echo(f"Client with name '{name}' not found.")
#     Session.close()
    
# @click.command()
# def search_car():
#     Session = SessionLocal()
#     model = input("Enter car model: ")
#     result = Session.query(Car).filter_by(model=model).first()
#     if result:
#         click.echo(f"Car found: {result.model}")
#     else:
#         click.echo(f"Car with model '{model}' not found.")
#     Session.close()


# @click.command()
# def search_employee():
#     session = SessionLocal()
#     name = input("Enter employee's name: ")
#     result = session.query(Employee).filter_by(name=name).first()
#     if result:
#         click.echo(f"Employee found: {result.name}")
#     else:
#         click.echo(f"Employee with name '{name}' not found.")
#     session.close()







cli.add_command(hello)
cli.add_command(add_client)
# cli.add_command(add_car)
# cli.add_command(add_employee)
# cli.add_command(search_client)
# cli.add_command(search_car)
# cli.add_command(search_employee)




if __name__ == '__main__':
    cli()
