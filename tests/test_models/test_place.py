#!/usr/bin/python3
"""Moddule to test for the instances of place."""
from tests.test_modules.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test for the instances of class Place."""

    def __init__(self, *args, **kwargs):
        """Initialize the self method of the class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test for the city value."""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test for the user value."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test for the name value."""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test for the description."""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_bathrooms(self):
        """Test for the number of bathrooms."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_number_of_rooms(self):
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_max_guest(self):
        """Test for the maximum number of guests."""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test for the price for each night."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test for the latitude of the location."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test for the longitude of the location."""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test for the list of amenities."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
