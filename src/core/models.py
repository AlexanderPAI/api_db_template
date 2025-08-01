from sqlalchemy import Column, String, Integer


from src.core.db import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
