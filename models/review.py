#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from sqlalchemy import Column, String, ForeignKey
    from models.base_model import Base

    class Review(BaseModel, Base):
        """This class defines review by various attributes for db"""
        __tablename__ = 'reviews'

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
else:
    class Review(BaseModel):
        """ Review class to store review information in file storage"""
        place_id = ""
        user_id = ""
        text = ""