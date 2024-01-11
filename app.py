from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import click

@click.command()
def hello():
    click.echo("hello maurine")

if __name__ =='__main__':
    hello()    

