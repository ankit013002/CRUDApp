from sqlalchemy import Column, Integer, String
from database import Base

class DataModel(Base):
    __tablename__ = "data_model"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    message = Column(String)
    email = Column(String, unique=True)

    def __init__(self, first_name=None, last_name=None, message=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.message = message
        self.email = email
