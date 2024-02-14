#!/usr/bin/python3
"""Module to test the instances of the amenities."""
from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Class for Amenity and to test its instances."""

    def __init__(self, *args, **kwargs):
        """Initialize the self method for the class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test for any new value."""
        new = self.value()
        self.assertEqual(type(new.name), str)
