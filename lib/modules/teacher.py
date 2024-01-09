


class Teacher():
    __tablename__='teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject_taught = Column(String)