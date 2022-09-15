#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')

    def __init__(self, *args, **kwargs):
        """initialize class instance"""
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = ''
        if 'state_id' in kwargs:
            self.state_id = kwargs['state_id']
        else:
            self.state_id = ''
        super().__init__(*args)
