#!/usr/bin/python3
"""Module for testing the review module."""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class for testing the instances of review."""

    def __init__(self, *args, **kwargs):
        """Initialize the self methods of class review."""
        super().__init__(self, *args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test for the place id."""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test for the user id."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test for text/strings."""
        new = self.value()
        self.assertEqual(type(new.text), str)
