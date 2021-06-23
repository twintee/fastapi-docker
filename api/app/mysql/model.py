# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import null
from .db import hndl_master, hndl_slave
from .base import Base

# userテーブルのモデルUserTableを定義
class UsersTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_login_at = Column(DateTime, nullable=True, default=null)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_valid = Column(Integer, nullable=False, default=1)
    __table_args__ = (Index(
        'idx_user_id_item_id', 'id', 'is_valid'),)

def get_db():
    db = hndl_slave.session()
    try:
        yield db
    finally:
        db.close()

def create(user):
    """
    Create user record
    """
    db = hndl_master.session()
    try:
        yield db
    finally:
        db.close()

def read(user):
    """
    Create user record
    """
    db = hndl_slave.session()
    try:
        yield db
    finally:
        db.close()
