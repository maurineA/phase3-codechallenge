


class Student():
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)