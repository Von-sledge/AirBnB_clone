#!/usr/bin/python3
"""Module for testing the city class."""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test for the basemodel."""

    def __init__(self, *args, **kwargs):
        """Initialize the self method."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test for state."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test for name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
