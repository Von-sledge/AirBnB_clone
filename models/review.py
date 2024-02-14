#!/usr/bin/python3
"""Public instance attribute: Review"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class atribute: Review"""

    place_id = ''
    user_id = ''
    text = ''
