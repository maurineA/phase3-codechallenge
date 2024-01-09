from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Teacher(Base):
    __tablename__='teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject_taught = Column(String)