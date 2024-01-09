

class Subject():
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)