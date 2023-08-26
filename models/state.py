#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

is_db = os.getenv("HBNB_TYPE_STORAGE") == 'db'


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if is_db:
        from models.city import City
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City', cascade='all, delete-orphan',
                backref='state')
    else:
        from models import storage
        name = ""

        @property
        def cities(self):
            """ A property that return list of all cities in database
            """
            return [
                    item['id'] for item in
                    storage.all().values()
                    if item['__class__'] == 'City' and
                    item['state_id'] == self.id]
