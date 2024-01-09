from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade_id = Column(Integer, ForeignKey('grades.id'))
    grade = relationship('Grade', back_populates='students')