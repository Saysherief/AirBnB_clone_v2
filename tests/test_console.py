#!/usr/bin/python3
"""Test Module for console.py

The console.py is a mudule that serves as interactive
terminal for various backend activities of the
AirBnB website
"""
import os
import json
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


    def test_do_create(self):
        """Test the do_create command

        The do_create command is used to create an
        object of given type
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            
            # skip if argument is unrecognized
            self.assertEqual(f.getvalue(),"")
            
            HBNBCommand().onecmd('create State name="California"')
            new_id = f.getvalue();

            HBNBCommand().onecmd("all State")
            response = f.getvalue();
            self.assertIn(
                    response,
                    new_id
                    )

