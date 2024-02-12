#!/usr/bin/python3
"""Test cases for console"""
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class Test_ConsoleCommand(unittest.TestCase):
    """To test all aspect of the console"""

    def test_prompting(self):
        "To check the HBNB command prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_class(self):
        """To check all class"""
        states = State()
        cities = City()
        places = Place()
        amenities = Amenity()
        reviews = Review()
        self.assertEqual(cities.__class__.__name__, "City")
        self.assertEqual(amenities.__class__.__name__, "Amenity")
        self.assertEqual(states.__class__.__name__, "State")
        self.assertEqual(reviews.__class__.__name__, "Review")
        self.assertEqual(places.__class__.__name__, "Place")

    def test_testBaseModel(self):
        """to test if BasesModels inherits all class correctly"""
        states = State()
        cities = City()
        places = Place()
        amenities = Amenity()
        reviews = Review()
        self.assertEqual(cities.__class__.__name__, "City")
        self.assertEqual(amenities.__class__.__name__, "Amenity")
        self.assertEqual(states.__class__.__name__, "State")
        self.assertEqual(reviews.__class__.__name__, "Review")
        self.assertEqual(places.__class__.__name__, "Place")


if __name__ == "__main__":
    unittest.main()
