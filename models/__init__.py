#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

is_db = os.getenv("HBNB_TYPE_STORAGE") == 'db'

if is_db:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
