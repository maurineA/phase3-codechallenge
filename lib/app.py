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
employees = Employee()
cars = Car()
#added hello test word to the cli group
@cli.command()  
def hello():
    click.echo("hello maurine")


#add client cli command
@cli.command()
@click.option('--name',prompt="Enter client's name", help="Enter client's name")
@click.option('--contact',prompt="Enter client's contact", help="Enter client's contact")
def add_client(name, contact):
     
    clients.add_client(name, contact)
   
    click.echo("Client added successfully!")
    
@cli.command()
@click.option('--name', prompt="Enter Employee's name", help="Enter Employee's name")
@click.option('--contact', type=int, prompt="Enter Employee's phone number", help="Enter Employee's phone number")
def add_employee(name, contact):
    
    employees.add_employee(name, contact)  
    click.echo("Employee added successfully!")

@cli.command()
@click.option('--type', prompt="Enter car type", help="Enter car type")
@click.option('--model', prompt="Enter car model", help="Enter car model")
@click.option('--color', prompt="Enter car color", help="Enter car color")
@click.option('--price', type=int, prompt="Enter car price", help="Enter car price")
@click.option('--client-id', type=int, prompt="Enter client's ID", help="Enter client's ID")
@click.option('--employee-id', type=int, prompt="Enter employee's ID", help="Enter employee's ID")
def add_car(type, model, color, price, client_id, employee_id):
    cars.add_car(type, model, color, price, client_id, employee_id)
    



@click.command()
@click.option('--name', prompt="Enter client's name", help="Enter client's name")
def search_client(name):
    clients.search_client_by_name(name)

    
@click.command()
@click.option('--name', prompt="Enter employee's name", help="Enter employee's name")
def search_employee(name):
    employees.search_employee(name)

@click.command()
@click.option('--model', prompt="Enter car's model", help="Enter car's model")
def search_car(model):
    cars.search_car_by_model(model)


@click.command()
@click.option('--name', prompt="Enter clients's name to delete", help="Enter clients's name to delete")
def delete_client(name):
    clients.delete_client(name)

@click.command()
@click.option('--name', prompt="Enter employee's name to delete", help="Enter employee's name to delete")
def delete_employee(name):
    employees.delete_employee(name)

@click.command()
@click.option('--model', prompt="Enter car's model to delete", help="Enter car's model to delete")
def delete_car(model):
    cars.delete_car(model)


cli.add_command(hello)
cli.add_command(add_client)
cli.add_command(add_car)
cli.add_command(add_employee)
cli.add_command(search_client)
cli.add_command(search_car)
cli.add_command(search_employee)
cli.add_command(delete_client)
cli.add_command(delete_employee)
cli.add_command(delete_car)





if __name__ == '__main__':
    cli()
    
