# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from random import choice
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

class DbHandler():

    DATABASE = 'mysql'
    def __init__(self, _user, _password, _host, _dbname, _port=3306) -> None:

        self.database = DbHandler.DATABASE

        if isinstance(_host, list):
            _host = choice(_host)
        self.db_url = f'{self.database}://{_user}:{_password}@{_host}:{_port}/{_dbname}'

        self.engine = create_engine(
                self.db_url,
                encoding="utf-8",
                echo=False)

        session = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine)
        self.session = session()
