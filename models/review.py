#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize class instance"""
        if 'place_id' in kwargs.keys():
            self.place_id = kwargs['place_id']
        else:
            self.place_id = ''
        if 'user_id' in kwargs.keys():
            self.user_id = kwargs['user_id']
        else:
            self.user_id = ''
        if 'text' in kwargs.keys():
            self.text = kwargs['text']
        else:
            self.text = ''
        super().__init__(*args)
