#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

is_file = os.getenv("HBNB_TYPE_STORAGE") == 'FileStorage'


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if not is_file:
        cities = relationship(
                'City', cascade='all, delete-orphan',
                backref='state')
    else:
        from models import storage

        @property
        def cities(self):
            """ A property that return list of all cities in database
            """
            return [
                    item['id'] for item in
                    storage.all().values()
                    if item['__class__'] == 'City' and
                    item['state_id'] == self.id]
