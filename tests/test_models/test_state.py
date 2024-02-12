#!/usr/bin/python3
"""Module for the state."""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Class for testing instances of state."""

    def __init__(self, *args, **kwargs):
        """Initialize the self method for state."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test for names."""
        new = self.value()
        self.assertEqual(type(new.name), str)
