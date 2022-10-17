#!/usr/bin/python3
"""
This module defines a class to manage
database storage for hbnb clone
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Class used to manage Database storage engine"""
    classes = ['State', 'City', 'User', 'Amenity', 'Place',
               'Review']

    __engine = None
    __session = None

    def __init__(self):
        """Creates the database storage engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
    if getenv('HBNB_ENV') == 'test':
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current db session for all objects
        depending on the classname argument cls
        """
        self.__session.query()
        objs = []
        obj_dict = {}
        if cls is not None:
            cls = eval(cls)
            objs.append(self.__session.query(cls))
        else:
            for cls_name in self.classes:
                objs.append(self.__session.query(eval(cls_name)))
        for cls_objs in objs:
            for obj in cls_objs:
                obj_dict[type(obj).__name__ + '.' + obj.id] = obj
                for clss in self.classes:
                    if ('_sa_instance_' + clss.lower()) in obj.__dict__:
                        del obj.__dict__['_sa_instance_' + clss.lower()]
                        break
        return obj_dict

    def new(self, obj):
        """
        add the object to the current
        database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current
        database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
         delete obj from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)
        return

    def reload(self):
        """
        Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        a public method def close(self):: call remove() method on
        the private session attribute (self.__session) tips or close()
        on the class Session
        """
        self.__session.close()
