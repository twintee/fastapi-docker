# -*- coding: utf-8 -*-
from os.path import join, abspath, dirname
import sys
import datetime as dt
from fastapi import FastAPI
from typing import List  # for nest body
from starlette.middleware.cors import CORSMiddleware

dir_sql = join(abspath(dirname(__file__)), 'sql')
sys.path.append(dir_sql)

from .mysql.db import hndl_master, hndl_slave
from .mysql.model import UsersTable



app = FastAPI()

# for CORS
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )

@app.get("/")
def root():

    return {
        "Hello": "World",
        "time": f"{dt.datetime.now()}"
        }

# テーブルにいる全ユーザ情報を取得 GET
@app.get("/users")
def read_users():
    users = hndl_slave.session.query(UsersTable).all()
    return users

