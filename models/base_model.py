#!/usr/bin/python3
"""BaseModel Module defines all common attributes/methods for classes of AirBnB clone."""

from uuid import uuid4
import datetime
#import models


class BaseModel:
    """
    BaseModel Module that defines all common attributes/methods.

    for other classes of AirBnB clone.
    Public instance attributes:\
    id: string - assign with an uuid when an instance is created.
    created_at: datetime - assign with the current datetime\
    when an instance is created.
    updated_at: datetime - assign with the current datetime when instance.
    is created and it will be updated every time you change your object.
    """

    def __init__(self):
        """Initialize BaseModel with unique ID."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datettime.today()

    def __str__(self):
        """Print: [<class name>] (<self.id>) <self.__dict__>."""
        cls_name = self.__class__.__name__
        return "[{}] [{}] [{}]".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Update the public instance update_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""
        cls = self.__dict__.copy()
        cls["__class__"] = self.__class__.__name__
        cls["created_at"] = self.created_at.isoformat()
        cls["updated_at"] = self.updated_at.isoformat()
        return cls
