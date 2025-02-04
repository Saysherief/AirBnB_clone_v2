#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    import sqlalchemy
    from sqlalchemy import Column, String
    from models.base_model import Base
    from sqlalchemy.orm import relationship

    class User(BaseModel, Base):
        """This class defines a user by various attributes for db"""
        __tablename__ = 'users'

        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
else:
    class User(BaseModel):
        """This class defines a user by various attributes for file"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
