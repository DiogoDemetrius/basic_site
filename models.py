from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Especifique o comprimento máximo
    password = Column(String(255))  # Especifique o comprimento máximo

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String(50))  # Especifique o comprimento máximo
    model = Column(String(50))  # Especifique o comprimento máximo
    year = Column(Integer)
    price = Column(Integer)
    description = Column(String(255))  # Especifique o comprimento máximo
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User")
