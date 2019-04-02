#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    @getter
    def cities:
        """getter for cities
        """
        all_cities = models.storage.all(City)
        cities = []
        for k, v in all_cities.items():
            if v.__state_id__ == self.id:
                cities.append(v)
        return cities
