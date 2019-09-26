from sqlalchemy import Column, Integer, String
from database import Base

class Contact(Base):
    __tablename__ = 'tb_contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)    
    phone_number = Column(Integer)
    email = Column(String)
    description = Column(String)
    
    def __init__(self, name, phone_number, email, description):        
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.description = description
    
    def __repr__(self):
        return "{},{},{},{}".format(self.name, self.phone_number, self.email, self.description)