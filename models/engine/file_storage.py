#!/usr/bin/python3
"""Class fileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file\
       and deserializes JSON file to instances.

       A private class attributes:
       a. __file_path
       b. __object

       Public instace methods:
       a. all(self)
       b. new(self, obj)
       c. save(self)
       d. reload(self)
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.is"""
        obj_name = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_name] = obj

    def save(self):
        """serializes __objects to the JSON file path"""
        json_file = {}
        for key, value in self.__objects.items():
            json_file[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dumps(json_file, f)

    def reload(self):
        """desrializes the JSON file to __objects if it exists"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_file = json.loads(f.read())
            for key, value in json_file.items():
                self.__objects[key] = eval(value['__class__'])(**value)
