#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        ret = {}
        if cls is not None:
            cls = eval(cls)
            name = cls.__name__
            for key, value in FileStorage.__objects.items():
                ob_name = key.split('.')
                if ob_name[0] == name:
                    if '_sa_instance_state' in value.__dict__.keys():
                        del value.__dict__['_sa_instance_state']
                    ret[key] = value
            return ret
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is not None:
            objj = obj.to_dict()['__class__'] + '.' + obj.id
            del self.__objects[objj]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """
         Call reload() method for deserializing the JSON file to objects
        """
        self.reload()
