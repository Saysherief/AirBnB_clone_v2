#!/usr/bin/python3
"""DBStorage Module

This module define a new storage engine 'DBStorage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

mysql_user = os.getenv("HBNB_MYSQL_USER")
mysql_user_pwd = os.getenv("HBNB_MYSQL_PWD")
mysql_host = os.getenv("HBNB_MYSQL_HOST")
mysql_db = os.getenv("HBNB_MYSQL_DB")
is_test_env = os.getenv("HBNB_ENV") == 'test'

class DBStorage:
    """A Relational database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                    mysql_user, mysql_user_pwd, mysql_host, mysql_db),
                pool_pre_ping=True)
        if is_test_env:
            db = self.__engine.cursor()
            session = sessionmaker(bind=self.__engine)()
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            for table_name in metadata.tables.keys():
                session.execute(f'DROP TABLE IF EXISTS {} CASCADE;')
            session.commit()

    def all(self, cls=None):
        """Query the database for all objects
        """

