#!/usr/bin/python3
"""Class fileStorage"""
import json
from models.base_model import BaseModel

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
    
    def reload(self):
        """desrializes the JSON file to __objects if it exists"""
