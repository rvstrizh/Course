from app.database import db

from marshmallow import Schema, fields
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer(), primary_key=True)
    name = Column(String())


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
