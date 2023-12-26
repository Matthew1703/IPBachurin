from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    numberOfPeople = Column(Integer)
    whereFrom = Column(Integer)
    whereTo = Column(Integer)
    data = Column(String)
    time = Column(String)
    phoneNumber = Column(String)
    money = Column(String)

    employee = Column(Integer, ForeignKey("employees.id"))

    def __repr__(self):
        return f"{self.name} - {self.numberOfPeople} - {self.whereFrom} - {self.whereTo} - {self.data} - {self.time} - {self}"


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    car = Column(String)

    def __repr__(self):
        return f"{self.name} - {self} - {self.car} - {self.application} - {self.time} - {self.data}"
