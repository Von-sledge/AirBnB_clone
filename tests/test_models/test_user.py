#!/usr/bin/python3
"""Module to test the instances of Class test_user."""
import test_models
from models.user import User


class test_User(test_basemodel):
    """Test various instances of user."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name - "User"
        self.value = User

    def test_first_name(self):
        """Test for the first name."""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test for the last name."""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test for the e-mail."""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test for the password."""
        new = self.value()
        self.assertEqual(type(new.password), str)
