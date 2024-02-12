#!/usr/bin/python3
"""Module for testing BaseModel."""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Class to test the instances of basemodel."""
    super().__init__(self, *args, **kwargs):
        """initialize the self method of basemodel."""
        super().__init__(*args, **kwargs)
        self.name   'BaseModel'
        self.value  BaseModel

    def setUp(self):
        """Test for setup."""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass

    def test_default(self):
        """Test for the default."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test for integer inputs."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test for save."""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as jsonFile:
            j = json.load(jsonFile)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test for string inputs."""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                       i.__dict__))

    def test_todict(self):
        """Test for dictionary."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test for kwargs."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test for kwargs for one input."""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test for ids."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test for a created_at."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_update_at(self):
        """Test for updated_at."""
        new = self.value()
        self.assertEqual(type(new.update_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
