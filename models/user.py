from datetime import datetime

from app import db, api
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, Float, Text
from flask_restx import fields


# DB固有の型はこう使う
# from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String(80), nullable=False)
    email = Column(String(40), nullable=False)
    birth_day = Column(Date, nullable=False, default=datetime.now)
    height = Column(Float, nullable=False, default=0.0)
    memo = Column(Text, nullable=False, default='')
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, nullable=False, default=True)


UserDto = api.model('UserDto', {
    'id': fields.Integer(min=0, description='primary_key'),
    'username': fields.String(min_length=0, max_length=80),
    'email': fields.String(min_length=0, max_length=40),
    'birth_day': fields.Date(example=datetime.now().strftime('%Y-%m-%d')),
    'height': fields.Float(example=0.0),
    'memo': fields.String(example='memo'),
    'created_at': fields.DateTime(example=datetime.now().strftime('%Y-%m-%dT%H:%M:%S')),
    'updated_at': fields.DateTime(example=datetime.now().strftime('%Y-%m-%dT%H:%M:%S')),
    'is_active': fields.Boolean,
})

UserInsertDto = api.model('UserInsertDto', {
    'username': fields.String(required=True, min_length=0, max_length=80),
    'email': fields.String(required=True, min_length=0, max_length=40),
    'birth_day': fields.Date(default=datetime.now().strftime('%Y-%m-%d')),
    'height': fields.Float(default=0.0),
    'memo': fields.String(default=''),
    'is_active': fields.Boolean(default=True),
})

UserUpdateDto = api.model('UserUpdateDto', {
    'username': fields.String(min_length=0, max_length=80),
    'email': fields.String(min_length=0, max_length=40),
    'birth_day': fields.Date(),
    'height': fields.Float(),
    'memo': fields.String(),
    'is_active': fields.Boolean(),
})
