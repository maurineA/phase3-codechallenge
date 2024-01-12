from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine
import click


engine = create_engine('sqlite:///car_wash.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@click.command()
def hello():
    click.echo("hello maurine")

if __name__ =='__main__':
    hello()    

@click.Command()
def add_employee():

