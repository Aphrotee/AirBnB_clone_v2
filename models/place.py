#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


"""place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))"""


class PlaceAmenity(Base):
    """place_amenities table"""
    __tablename__ = 'place_amenity'
    place_id = Column(String(60),
                      ForeignKey('places.id'),
                      primary_key=True, nullable=False)
    amenities_id = Column(String(60),
                          ForeignKey('amenities.id'),
                          primary_key=True, nullable=False)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 viewonly=True)

    def __init__(self, *args, **kwargs):
        """initialize class instance"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Review setter"""
            from models import storage
            review_obj = storage.all('Review')
            ret = []
            for key, value in review_obj.items():
                if self.id == value.place_id:
                    ret.append(value)
            return ret

        @property
        def amenities(self):
            """Amenities getter"""
            from models import storage
            amenity_obj = storage.all('Amenity')
            ret = []
            for key, value in amenity_obj.items():
                if value.id in self.amenity_ids:
                    ret.append(value)
            return ret

        @amenities.setter
        def amenities(self, obj=None):
            """Amenities setter"""
            print("in setter")
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
