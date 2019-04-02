#!/usr/bin/python3
""" Database storage engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
import os


class DBStorage:
    """ Database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """ initializes DBStorage class
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                        os.environ['HBNB_MYSQL_USER'],
                                        os.environ['HBNB_MYSQL_PWD'],
                                        os.environ['HBNB_MYSQL_HOST'],
                                        os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """ query on current db session all objects depending on class name
            Return: dictionary with <class-name>.<object-id> : <object>
        """
        obj_dict = {}
        if cls is None:
            classes = self.__session.query(User, State, City, Amenity, Place, Review).\
                all();
        else:
            classes = self.__session.query(cls).all()
        for obj in classes:
            key = obj.__name__ + '.' + obj.__id__
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables, and current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
