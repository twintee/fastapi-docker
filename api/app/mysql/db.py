# -*- coding: utf-8 -*-
from .dbhandler import DbHandler as dbhndl

USER = 'user'
PASSWORD = 'GUJcVMZvS47UIrHwnxCVkLOWS42DFw'

HOST_M = '172.29.71.175'
PORT_M = '3306'
HOST_S = ['172.29.71.175']
PORT_S = '3307'

DB_NAME = 'main'

hndl_master = dbhndl(
        _user=USER,
        _password=PASSWORD,
        _host=HOST_M,
        _dbname=DB_NAME,
        _port=PORT_M
        )

hndl_slave = dbhndl(
        _user=USER,
        _password=PASSWORD,
        _host=HOST_S,
        _dbname=DB_NAME,
        _port=PORT_S
        )
# session_master = sessionmaker(
#         autocommit=False,
#         autoflush=False,
#         bind=hndl_master.engine)

# session_slave = sessionmaker(
#         autocommit=False,
#         autoflush=False,
#         bind=hndl_slave.engine)

