#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """initialize class instance"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """City getter"""
            from models import storage
            city_obj = storage.all('City')
            ret = []
            for key, value in city_obj.items():
                if self.id == value.state_id:
                    ret.append(value)
            return ret
