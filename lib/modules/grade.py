from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from . import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    grade_number = Column(Integer)