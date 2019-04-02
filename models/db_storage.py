#!/usr/bin/python3
""" Database storage engine
"""



class DBStorage:
    """ Database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """ initializes DBStorage class
        """

    def all(self, cls=None):
        """ query on current db session all objects depending on class name
            Return: dictionary with <class-name>.<object-id> : <object>
        """

    def new(self, obj):
        """ add object to current database session
        """

    def save(self):
        """ commit all changes of current database session
        """

    def delete(self, obj=None):
        """ delete from current database session
        """

    def reload(self):
        """ create all tables, and current database session
        """
