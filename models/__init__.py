#!/usr/bin/python3
"""Creates a unique instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
