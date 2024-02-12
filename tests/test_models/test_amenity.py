#!/usr/bin/python3
"""Module to test the instances of the amenities."""
from tests.test_model import test_basemodel
from model.amenity import Amenity


class test_Amenity(test_basemodel):
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
