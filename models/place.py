#!/usr/bin/python3
"""This is the place class"""
import models
import os
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel, Base


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: price for staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
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
    reviews = relationship("Review", cascade="all,delete", backref="place")

    @property
    def reviews(self):
        """ filestorage reviews getter
        """
        all_reviews = models.storage.all(Review)
        places = []
        for k, v in all_reviews.items():
            if v.__place_id__ == self.id:
                places.append(v)
        return places

    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """ getter attribute for amenity based on file storage
            """
            all_amenities = models.storage.all(Amenity)
            places = []
            for k, v in all_amenities.items():
                if v.id in self.amenity_ids:
                    places.append(v)
            return places

        @amenities.setter
        def amenities(self, amn):
            """ setter attribute for amenities based on file storage
            """
            if type(amn) is Amenity:
                self.amenity_ids.append(str(amn.id))
