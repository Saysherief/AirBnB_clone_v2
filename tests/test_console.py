#!/usr/bin/python3
"""Test Module for console.py

The console.py is a mudule that serves as interactive
terminal for various backend activities of the
AirBnB website
"""
import os
import uuid
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage

class ConsoleTest(TestCase):
    """Define different tests for console
    """

    @classmethod
    def setUpClass(cls):
        attr_map = FileStorage.__dict__
        storage_name = attr_map["_FileStorage__file_path"]
        
        backup = str(uuid.uuid4()).replace("-", "")
        cls.store_exist = False
        cls.storage_name = storage_name

        if os.path.exists(storage_name):
            cls.store_exist = True
            print("creating backup... ", end="")
            os.rename(storage_name, backup)
            open(storage_name, "w").close()
            cls.backup = backup
            print("[ok]")
        else:
            print("creating test storage... ", end="")
            open(storage_name, "w").close()
            print("[ok]")

    @classmethod
    def tearDownClass(cls):
        print()
        print("removing test storage...", end="")
        os.remove(cls.storage_name)
        print("[ok]")

        if cls.store_exist:
            print("restoring backup... ", end="")
            os.rename(cls.backup, cls.storage_name)
            print("[ok]")


    def test_invalid_class(self):
        """Test the do_create command

        The do_create command is used to create an
        object of given type
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            
            # skip if argument is unrecognized
            self.assertIn(
                    "class doesn't exist",
                    f.getvalue())

    def test_valid_class_one_attribute(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            new_id = f.getvalue().strip();
            HBNBCommand().onecmd("all State")
            response = f.getvalue()
            self.assertIn(new_id, response)
    
    def test_valid_class_attribute_underscore(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="My_house"')
            response2 = f.getvalue().strip()
            HBNBCommand().onecmd("all State")
            self.assertIn("My house", f.getvalue().strip())

    def test_valid_class_multiple_attributes(self):    
        with patch('sys.stdout', new=StringIO()) as f:    
            data = (
                    'create State name="My"house" ' +
                    'age="35" location_id="00015" ' +
                    'invalid_name=" This name"'
                    )

            HBNBCommand().onecmd(data)
            HBNBCommand().onecmd("all State")
            result = f.getvalue().strip()
            self.assertNotIn("invalid_name", result)
